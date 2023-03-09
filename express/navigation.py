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
            self.wait_for_element_presence((By.TAG_NAME, 'body'))

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
        element = self.determine_locator(element)
        try:
            self.wait_for_element_presence(element)
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
        element = self.determine_locator(element)
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
