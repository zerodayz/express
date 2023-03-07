import pytest as pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import logging
from src import express


class Express:
    def __init__(self, driver_name, caplog):
        self.driver = None
        self.actions = None

        self._init_driver(driver_name, caplog)

    def _init_driver(self, browser_to_run, caplog):
        """Create a driver instance based on the browser to run."""

        services = {
            'chrome': ChromeService(ChromeDriverManager().install()),
            'firefox': FirefoxService(GeckoDriverManager().install())
        }
        options = {
            'chrome': webdriver.ChromeOptions(),
            'firefox': webdriver.FirefoxOptions()
        }
        options[browser_to_run].add_argument('--headless=new')
        if browser_to_run not in services:
            raise Exception(f'Browser {browser_to_run} is not supported.')

        self.driver = webdriver.__dict__[browser_to_run.capitalize()](service=services[browser_to_run],
                                                                      options=options[browser_to_run])
        self.actions = express.Actions(self.driver, caplog)


def pytest_addoption(parser):
    """CLI args which can be used to run the tests with specified values."""
    parser.addoption('--browser', action="append", default=[], choices=['chrome', 'firefox'],
                     help='Your choice of browser '
                          'to run tests.')


def pytest_generate_tests(metafunc):
    """To generate the parametrized tests"""
    browsers = metafunc.config.getoption("browser")
    if "browser_to_run" in metafunc.fixturenames:
        metafunc.parametrize("browser_to_run", browsers)


@pytest.fixture(autouse=True)
def actions(browser_to_run, caplog):
    """Create an instance of Express class and return it to the test."""
    x = Express(browser_to_run, caplog)
    yield x.actions
    x.driver.quit()
