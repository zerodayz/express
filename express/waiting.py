import contextlib
import logging
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from express import expected_conditions as EC2

from express import utils


class Waiting:
    def wait_for(self, element, timeout=60, condition=None):
        """
        This function waits for the element to match the condition.

        Params:
            element (tuple): The element to wait for.
            timeout (int): The timeout in seconds.
            condition (function): The condition to wait for.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        element = self.find_locator(element)
        try:
            WebDriverWait(self.driver, timeout).until(condition(element))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def wait_for_selection_of_element(self, element, timeout=60):
        """
        This function waits for the element to be selected.

        Params:
            element (tuple): The element to wait for.
            timeout (int): The timeout in seconds.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        self.wait_for(element, timeout=timeout, condition=EC.element_located_to_be_selected)

    def sleep_between(self, w_min, w_max):
        """
        This function waits for a random amount of time between min and max.

        Params:
            w_min (int): The minimum amount of time to wait.
            w_max (int): The maximum amount of time to wait.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        try:
            time.sleep(random.randint(w_min, w_max))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def wait_for_attribute_of_element(self, element, attribute, value, timeout=60):
        """
        This function waits for an element to have a attribute with a value.

        Params:
            element (str): An element locator.
            attribute (str): The name of the attribute.
            value (str): The value of the attribute.
            timeout (int): The number of seconds to wait before timing out.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        element = self.find_locator(element)
        try:
            WebDriverWait(self.driver, timeout).until(EC2.element_attribute_is(element, attribute, value))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def wait_for_visibility_of_element(self, element, timeout=60):
        """
        This function waits for an element to be visible on the web page.

        Params:
            element (str): An element locator.
            timeout (int): The number of seconds to wait before timing out.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        self.wait_for(element, timeout=timeout, condition=EC.visibility_of_element_located)

    def wait_for_presence_of_element(self, element, timeout=60):
        """
        This function waits for an element to be present on the web page.

        Params:
            element (str): An element locator.
            timeout (int): The number of seconds to wait before timing out.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        self.wait_for(element, timeout=timeout, condition=EC.presence_of_element_located)

    def wait_for_clickable_element(self, element, timeout=60):
        """
        This function waits for an element to be clickable on the web page.

        Params:
            element (str): An element locator.
            timeout (int): The number of seconds to wait before timing out.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        self.wait_for(element, timeout=timeout, condition=EC.element_to_be_clickable)

    @contextlib.contextmanager
    def wait_for_page_to_load(self, timeout=60):
        """
        This function checks if the page loaded. It only works for non-javascript click.
        Meaning you need to get the new html element after the click.

        Params:
            None

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        try:
            old_page = self.driver.find_element(By.TAG_NAME, "body")
            yield
            WebDriverWait(self.driver, timeout).until(EC.staleness_of(old_page))

        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e
