from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from express import utils


class Base:
    def click(self, element):
        """
        Click on an element.

        Args:
            element (string): String representing the element to be clicked

        Returns:
            None

        Raises:
            Exception: If element not found or if any exception occurs
        """
        element = self.determine_locator(element)
        try:
            self.wait_for_element_clickable(element)
            self.driver.find_element(*element).click()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def hover(self, element):
        """
        This function hovers to an element on the page and performs an action.

        Args:
            element: The element to be hovered.

        Returns:
            None.

        Raises:
            Exception: If any error occurs.
        """
        element = self.determine_locator(element)
        try:
            self.wait_for_element_presence(element)
            # The move_to_element action does not work in Firefox unless the element is scrolled into view.
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))
            hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*element))
            hover.perform()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def move_mouse_to_element(self, element):
        """
        This function moves the mouse to the given element.

        Params:
            element (str): An element locator.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        element = self.determine_locator(element)
        try:
            ActionChains(self.driver).move_to_element(self.driver.find_element(*element)).perform()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def move_mouse_to(self, x, y):
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

    def drag_and_drop(self, element_from, element_to):
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
        element_from = self.determine_locator(element_from)
        element_to = self.determine_locator(element_to)
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(element_from))
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(element_to))
            ActionChains(self.driver).drag_and_drop(self.driver.find_element(*element_from),
                                                    self.driver.find_element(*element_to)).perform()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def type(self, element, text):
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
        element = self.determine_locator(element)
        try:
            self.wait_for_element_presence(element)
            self.driver.find_element(*element).send_keys(text)
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def remove_highlight(self, element, style=None):
        """
        This function clears the highlight from the given element on the web page.

        Args:
           element (tuple): The highlighted element to be cleared.
           style (str): The style to use for the highlight.

        Returns:
           None

        Raises:
           Exception: If the element is not located on the page.
        """
        locator = self.determine_locator(element)
        # If no style was specified, just reset the style to an empty string.
        # otherwise, use the style that was specified.
        if style is None:
            style = ''
        else:
            style = style
        try:
            self.wait_for_element_presence(locator)
            self.driver.execute_script("arguments[0].style = arguments[1];",
                                       self.driver.find_element(*locator), style)

        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def highlight(self, element, style="border: 2px solid rgb(255, 0, 0);"):
        """
        This function highlights the given element on the web page.

        Args:
           element (tuple): The element to be highlighted.
           style (str): The style to use for the highlight.

        Returns:
           None

        Raises:
           Exception: If the element is not located on the page.
        """
        locator = self.determine_locator(element)
        # validate css style
        style = self.validate_style(style)
        try:
            self.wait_for_element_presence(locator)
            # remove any color transition from the element https://github.com/SeleniumHQ/selenium/issues/11740
            # and update the element style to the given style
            self.driver.execute_script("arguments[0].style = arguments[1];",
                                       self.driver.find_element(*locator),
                                       style + "transition: none !important;")

        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e
