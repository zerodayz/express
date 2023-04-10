import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from express import utils


class Navigation:
    def go(self, url):
        """
        Navigates the web driver to the given URL, and waits for the page to load.

        Params:
            url (str): The URL that the browser should navigate to.

        Returns:
            None

        Raises:
            Exception: If there was an error loading the page.
        """
        self.driver.get(url)
        try:
            self.wait_for_presence_of_element((By.TAG_NAME, 'body'))

        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def scroll_down_by_y(self, y):
        """
        This function scrolls down by a given amount.

        Params:
            y (int): The amount to scroll down by.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        try:
            self.driver.execute_script("window.scrollBy(0, {});".format(y))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def scroll_up_by_y(self, y):
        """
        This function scrolls up by a given amount.

        Params:
            y (int): The amount to scroll up by.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        try:
            self.driver.execute_script("window.scrollBy(0, -{});".format(y))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def scroll_left_by_x(self, x):
        """
        This function scrolls left by a given amount.

        Params:
            x (int): The amount to scroll left by.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        try:
            self.driver.execute_script("window.scrollBy(-{}, 0);".format(x))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def scroll_right_by_x(self, x):
        """
        This function scrolls right by a given amount.

        Params:
            x (int): The amount to scroll right by.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        try:
            self.driver.execute_script("window.scrollBy({}, 0);".format(x))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def scroll_into_element(self, element):
        """
        This function is waiting for it to be present before executing the script.

        Params:
            element (tuple): The element to be scrolled into view.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        element = self.find_locator(element)
        try:
            self.wait_for_presence_of_element(element)
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def scroll_to_bottom_page(self):
        """
        This function scrolls to the bottom of the page.

        Params:
            None

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def scroll_to_top_page(self):
        """
        This function scrolls to the top of the page.

        Params:
            None

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def get_href(self, locator):
        """
        This function gets the href attribute of an element.

        Params:
            locator (tuple): The locator of the element.

        Returns:
            str: The href attribute of the element.

        Raises:
            Exception: In case of any error.
        """
        element = self.find_locator(locator)
        try:
            self.wait_for_presence_of_element(element)
            link = self.driver.find_element(*element).get_attribute("href")
            logging.getLogger().info("Link on element: {}: link {}".format(element, link))
            return link

        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def switch_to_frame(self, frame):
        """
        This function switches the web driver to the given frame.

        Params:
            frame (str): The frame to switch to.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        try:
            self.driver.switch_to.frame(frame)
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def switch_to_iframe(self, element):
        """
        This function switches the web driver to the given iframe.

        Params:
            element (str): The iframe to switch to.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        element = self.find_locator(element)
        try:
            WebDriverWait(self.driver, 60).until(EC.frame_to_be_available_and_switch_to_it(element))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def switch_to_default_content(self):
        """
        This function switches the web driver to the default content.

        Params:
            None

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e
