import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class InputMethod:
    def mouse_click(self, element):
        """
        Click on an element.

        Args:
            element (string): String representing the element to be clicked

        Returns:
            None

        Raises:
            Exception: If element not found or if any exception occurs
        """
        element = self.find_locator(element)
        logging.getLogger().info("Clicking on element: {}".format(element))
        try:
            self.wait_for_clickable_element(element)
            self.driver.find_element(*element).click()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def mouse_hover(self, element):
        """
        This function hovers to an element on the page and performs an action.

        Args:
            element: The element to be hovered.

        Returns:
            None.

        Raises:
            Exception: If any error occurs.
        """
        element = self.find_locator(element)
        try:
            self.wait_for_presence_of_element(element)
            # The move_to_element action does not work in Firefox unless the element is scrolled into view.
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))
            hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*element))
            hover.perform()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def mouse_move_to_element(self, element):
        """
        This function moves the mouse to the given element.

        Params:
            element (str): An element locator.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        element = self.find_locator(element)
        try:
            ActionChains(self.driver).move_to_element(self.driver.find_element(*element)).perform()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def upload_file(self, element, file_path):
        """
        This function uploads a file.

        Args:
            element (str): The element to upload the file to.
            file_path (str): The path to the file to upload.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        element = self.find_locator(element)
        try:
            self.driver.find_element(*element).send_keys(file_path)
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def mouse_move_to_xy_coordinates(self, x, y):
        """
        This function moves the mouse to the given coordinates.

        Args:
            x (int): The x coordinate to move the mouse to.
            y (int): The y coordinate to move the mouse to.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        try:
            ActionChains(self.driver).move_by_offset(x, y).perform()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def mouse_drag_and_drop(self, element_from, element_to):
        """
        This function drags an element to another element.

        Args:
            element_from (str): The element to drag.
            element_to (str): The element to drop the first element on.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        element_from = self.find_locator(element_from)
        element_to = self.find_locator(element_to)
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(element_from))
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(element_to))
            ActionChains(self.driver).drag_and_drop(self.driver.find_element(*element_from),
                                                    self.driver.find_element(*element_to)).perform()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def keyboard_press(self, key):
        """
        This function will press a key on the keyboard.

        Args:
            key (str): The key to press.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        try:
            ActionChains(self.driver).send_keys(key).perform()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def keyboard_type(self, element, text):
        """
        This function will type text into an element on a web page.

        Args:
            element (str): An element locator.
            text (str): The text to type into the element.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        element = self.find_locator(element)
        try:
            self.wait_for_presence_of_element(element)
            self.driver.find_element(*element).clear()
            self.driver.find_element(*element).send_keys(text)
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e
