import json
import logging
import random
import shutil
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

from src import utils
import os
"""
  Constants for the Actions class
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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


def validate_style(style):
    """
    This function validates the given style.

    Args:
       style (str): The style to validate.

    Returns:
       str: The validated style.

    Raises:
       Exception: If the style is not valid.
    """
    if not style.endswith(";"):
        style = style + ";"
    return style


class Actions:

    def __init__(self, driver, caplog):
        
        self.driver = driver
        self.caplog = caplog

        self.username = None
        self.password = None
        self.test_dir = None
        self.dir = BASE_DIR
        self.dir_in = os.path.join(BASE_DIR, 'in')
        self.dir_out = os.path.join(BASE_DIR, 'out')

    """
      System methods
    """

    def set_credentials(self, username, password):
        """
        Sets the username and password for the actions class

        Params:
            username (str): The username to be used
            password (str): The password to be used

        Returns:
            None
        """
        
        self.username = username
        self.password = password

    def prepare_tests(self, test_name):
        self.test_dir = os.path.join(self.dir_out, test_name)

    """
      Testing functions
    """

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
        # wait for the page to load
        try:
            self.wait_for_element((By.TAG_NAME, 'body'))
            
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
        element = determine_locator(element)
        try:
            self.wait_for_element(element)
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def take_screenshot(self, filename, element="tag=body",
                        highlight=False, highlight_element=None, highlight_style="border: 2px solid rgb(255, 0, 0);",
                        annotate_text=None):
        """
        This function takes a screenshot of the web page and saves it in filename.

        Params:
            locator (string): Name of the element to take a screenshot of.
            filename (string): Name of the file to save the screenshot.
            highlight (bool): If true, the element will be highlighted before taking the screenshot.
            highlight_style (string): The style to use for the highlight.
            annotate_text (string): Text to annotate the screenshot with.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        if self.username:
            user_path = os.path.join(self.test_dir, self.driver.name.capitalize(), self.username)
        else:
            user_path = os.path.join(self.test_dir, self.driver.name.capitalize())
        os.makedirs(user_path, exist_ok=True)
        filepath = os.path.join(user_path, filename)
        try:
            # if the element is the body, take a screenshot of the whole page
            if element == "tag=body":
                if highlight and highlight_element:
                    highlight_element = determine_locator(highlight_element)
                    # save the original style of the element
                    original_style = self.get_style(highlight_element)

                    self.highlight(highlight_element, style=highlight_style)
                    self.driver.save_screenshot(filepath)
                    self.remove_highlight(highlight_element, style=original_style)
                else:
                    self.driver.save_screenshot(filepath)
            else:
                if highlight and highlight_element:
                    highlight_element = determine_locator(highlight_element)
                    # save the original style of the element
                    original_style = self.get_style(highlight_element)

                    self.highlight(highlight_element, style=highlight_style)
                    self.driver.find_element(*element).screenshot(filepath)
                    self.remove_highlight(highlight_element, style=original_style)
                else:
                    self.driver.find_element(*element).screenshot(filepath)

            # annotate the screenshot
            if annotate_text:
                utils.annotate(filepath, annotate_text)
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
        element = determine_locator(element)
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

    def wait_between(self, w_min, w_max):
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

    def wait_for_style(self, element, style, timeout=60):
        """
        This function waits for an element to have a specific style.

        Params:
            element (str): An element locator.
            style (str): The style to wait for.
            timeout (int): The number of seconds to wait before timing out.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        element = determine_locator(element)
        try:
            WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(element, style))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def get_style(self, element):
        """
        This function gets the style of an element.

        Params:
            element (str): An element locator.

        Returns:
            str: The style of the element.

        Raises:
            Exception: In case of any error.
        """
        locator = determine_locator(element)
        try:
            self.wait_for_element(locator)
            return self.driver.find_element(*locator).get_attribute("style")
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def wait_for_element(self, element, timeout=60):
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
        element = determine_locator(element)
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(element))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def wait_for_page_to_load(self, url):
        """
        This function checks if the current page URL is the same as the given URL.

        Params:
            url (str): The URL to check.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        try:
            old_page = self.driver.find_element(by=By.TAG_NAME, value='body')
            WebDriverWait(self.driver, 60).until(EC.url_to_be(url))
            # check if the new webpage was loaded
            WebDriverWait(self.driver, 60).until(EC.staleness_of(old_page))

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
        element = determine_locator(element)
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
        element_from = determine_locator(element_from)
        element_to = determine_locator(element_to)
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
        element = determine_locator(element)
        try:
            self.wait_for_element(element)
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
        locator = determine_locator(element)
        # If no style was specified, just reset the style to an empty string.
        # otherwise, use the style that was specified.
        if style is None:
            style = ''
        else:
            style = style
        try:
            self.wait_for_element(locator)
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
        locator = determine_locator(element)
        # validate css style
        style = validate_style(style)
        try:
            self.wait_for_element(locator)
            # remove any color transition from the element https://github.com/SeleniumHQ/selenium/issues/11740
            # and update the element style to the given style
            self.driver.execute_script("arguments[0].style = arguments[1];",
                                       self.driver.find_element(*locator),
                                       style + "transition: none !important;")

        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

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
        element = determine_locator(element)
        # Check the element is type XPath
        if element[0] != "xpath":
            self.driver.quit()

            raise Exception(f"element '{element}' is not of type XPath. Please use XPath element.")
        try:

            self.wait_for_element(element)
            # find the nearest wrapping element that can be highlighted
            return element[0], element[1] + "/.."
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

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
        element = determine_locator(element)
        try:

            self.wait_for_element(element)

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
        element = determine_locator(element)
        try:
            self.wait_for_element(element)
            # The move_to_element action does not work in Firefox unless the element is scrolled into view.
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))
            hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*element))
            hover.perform()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def load_json(self, filename):
        """
        This function loads a JSON file and returns the data.

        Args:
            filename (str): The name of the JSON file.

        Returns:
            dict: The data from the JSON file.

        Raises:
            Exception: If there is an error loading the JSON file.
        """
        try:
            with open(os.path.join(self.dir_in, filename)) as f:
                return json.load(f)
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def login(self, url, username=None, password=None,
              username_locator="name=username", password_locator="name=password",
              submit="name=submit"):
        """
        Logs into the website using the provided username and password

        Args:
            url (str): The URL of the website
            username_locator (str): The locator for the username field
            username (str): The username for authenticating the account
            password_locator (str): The locator for the password field
            password (str): The password for authenticating the account
            submit (str): The locator for the login button

        Returns:
            None

        Raises:
            Exception: If there is an error while logging in
        """
        self.go(url)
        if self.username is not None:
            username = self.username
        if self.password is not None:
            password = self.password
        self.type(username_locator, username)
        self.type(password_locator, password)
        self.click(submit)
        # wait for the page to load
        try:
            self.wait_for_element((By.TAG_NAME, 'body'))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e
