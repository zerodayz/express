import contextlib
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Identification:
    def find_nearest_xpath(self, element):
        """
        The checkbox can't be highlighted, we need to find the nearest element that can be.

        Args:
            element (string): String representing the inner element of the element
                              to be highlighted (xpath)

        Returns:
            tuple: The nearest element that can be highlighted

        Raises:
            Exception: If element not found or if any exception occurs
        """
        element = self.determine_locator(element)
        # Check the element is type XPath
        if element[0] != "xpath":
            self.driver.quit()

            raise Exception(f"element '{element}' is not of type XPath. Please use XPath element.")
        try:

            self.wait_for_presence_of_element(element)
            # find the nearest wrapping element that can be highlighted
            return element[0], element[1] + "/.."
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def element_exists(self, element):
        """
        This function checks if an element exists on the page.

        Args:
            element (string): String representing the element to be checked

        Returns:
            bool: True if element exists, False otherwise

        Raises:
            Exception: If element not found or if any exception occurs
        """
        try:
            self.wait_for(element, timeout=10, condition=EC.presence_of_element_located)
            return True
        except Exception as e:
            print("Error handled: ", e)
            return False

    @staticmethod
    def determine_locator(element):
        """
        This function determines the locator used to find an element on a web page.

        Params:
            locator (str): The locator used to locate an element on a web page.

        Returns:
            By (object): An object of the selenium.webdriver.common.by class.
            Name (str): The name of the locator.

        Raises:
            ValueError: If the locator prefix is invalid.
        """
        # Do not convert if the element is already a locator (tuple)
        if isinstance(element, tuple):
            return element
        locator_dict = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "css": By.CSS_SELECTOR,
            "xpath": By.XPATH,
            "linkText": By.LINK_TEXT,
            "partial_link": By.PARTIAL_LINK_TEXT,
            "tag": By.TAG_NAME,
        }
        locator_prefix = element.split('=')[0]
        locator_name = '='.join(element.split('=')[1:])

        if locator_prefix not in locator_dict.keys():
            raise ValueError("Invalid locator prefix: {}".format(locator_prefix))

        return locator_dict[locator_prefix], locator_name

