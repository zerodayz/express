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

        services = {
            'chrome': ChromeService(ChromeDriverManager().install()),
            'firefox': FirefoxService(GeckoDriverManager().install())
        }
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
