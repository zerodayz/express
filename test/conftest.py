import os
import re

import pytest as pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import logging
from express import Actions


class Express:
    def __init__(self, driver_name, headless, caplog):
        self.driver = None
        self.actions = None

        self._init_driver(driver_name, headless, caplog)

    def _init_driver(self, browser_to_run, headless, caplog):
        """Create a driver instance based on the browser to run."""

        # It seems that the ChromeDriverManager().install() although loading drivers from cache,
        # still talk to GitHub API to get the latest version of the driver. This exhausts the API request limit.
        services = {}

        # This is ugly, ugly workaround, but it gets the job done... now.
        # # get driver _get_driver_path
        if browser_to_run == 'chrome':
            metadata_items = ChromeDriverManager().driver_cache.get_metadata()
            # check the last timestamp of the driver in cache
            if metadata_items:
                # sort metadata_path by timestamp
                sorted_metadata_items = sorted(metadata_items.items(), key=lambda x: x[1]['timestamp'])
                # find the latest driver path which ends with chromedriver
                for item in sorted_metadata_items:
                    if re.search(r'chromedriver', item[1]['binary_path']):
                        chrome_driver_path = item[1]['binary_path']
                        break
            if chrome_driver_path:
                services['chrome'] = ChromeService(chrome_driver_path)
            else:
                services['chrome'] = ChromeService(ChromeDriverManager().install())
            logging.getLogger().info(chrome_driver_path)
        elif browser_to_run == 'firefox':
            metadata_items = GeckoDriverManager().driver_cache.get_metadata()
            # check the last timestamp of the driver in cache
            if metadata_items:
                # sort metadata_path by timestamp
                sorted_metadata_items = sorted(metadata_items.items(), key=lambda x: x[1]['timestamp'])
                # get the latest driver path
                for item in sorted_metadata_items:
                    if re.search(r'geckodriver', item[1]['binary_path']):
                        firefox_driver_path = item[1]['binary_path']
                        break
            if firefox_driver_path:
                services['firefox'] = FirefoxService(firefox_driver_path)
            else:
                services['firefox'] = FirefoxService(GeckoDriverManager().install())
            logging.getLogger().info(firefox_driver_path)

        options = {
            'chrome': webdriver.ChromeOptions(),
            'firefox': webdriver.FirefoxOptions()
        }

        if headless and browser_to_run == 'chrome':
            options[browser_to_run].add_argument('--headless=new')
        elif headless and browser_to_run == 'firefox':
            options[browser_to_run].add_argument('-headless')

        if browser_to_run not in services:
            raise Exception(f'Browser {browser_to_run} is not supported.')

        self.driver = webdriver.__dict__[browser_to_run.capitalize()](service=services[browser_to_run],
                                                                      options=options[browser_to_run])
        self.actions = Actions(self.driver, caplog)


def pytest_addoption(parser):
    """CLI args which can be used to run the tests with specified values."""
    parser.addoption('--browser', action="append", default=[], choices=['chrome', 'firefox'],
                     help='Your choice of browser '
                          'to run tests.')
    parser.addoption('--headless', action="store_true", default=False, help='Run tests in headless mode.')


def pytest_generate_tests(metafunc):
    """To generate the parametrized tests"""
    browsers = metafunc.config.getoption("browser")
    if "browser_to_run" in metafunc.fixturenames:
        metafunc.parametrize("browser_to_run", browsers)


@pytest.fixture(autouse=True)
def actions(request, browser_to_run, caplog):
    """Create an instance of Express class and return it to the test."""
    headless = request.config.getoption("headless")

    x = Express(browser_to_run, headless, caplog)

    # prepare the test
    full_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
    result = re.findall(r"test_\w+", full_name)[0]
    if headless:
        logging.getLogger().info(f'Running test {result} on {browser_to_run} browser in headless mode.')
    else:
        logging.getLogger().info(f'Running test {result} on {browser_to_run} browser.')
    x.actions.prepare_tests(result)

    # execute the test
    yield x.actions

    logging.getLogger().info(f'Finished test {result} on {browser_to_run} browser.')
    x.driver.quit()
