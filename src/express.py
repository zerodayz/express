import json
import shutil
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

import os

"""
  Constants for the Actions class
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Actions:

    def __init__(self, driver):
        self.driver = driver
        self.username = None
        self.password = None
        self.test_dir = None
        # set the log level to debug or info
        self.log_level = "debug"
        self.dir = BASE_DIR
        self.dir_in = os.path.join(BASE_DIR, 'in')
        self.dir_out = os.path.join(BASE_DIR, 'out')

    """
      System methods
    """

    def logger(self, level, message):
        """
        Logs a message with a time stamp and given log level

        Params:
            level (str): The log level to be used
            message (str): The message to be logged

        Returns:
            None
        """
        # if log_level is set to debug, print all messages
        if self.log_level == "debug":
            current_time = time.strftime("%d/%m/%Y %H:%M", time.localtime())
            print(f"{current_time} [{level}] {message}")
        # if log_level is set to info, print only info and error messages
        elif self.log_level == "info" and level in ["info", "error"]:
            current_time = time.strftime("%d/%m/%Y %H:%M", time.localtime())
            print(f"{current_time} [{level}] {message}")

    def prepare_tests(self, test_name):
        self.test_dir = os.path.join(self.dir_out, test_name)

    """
      Testing functions
    """

    def determine_locator(self, element):
        """
        This function determines the locator used to find an element on a web page.

        Params:
        locator (str): The locator used to locate an element on a web page.

        Returns:
        By (object): An object of the selenium.webdriver.common.by class.
        Name (str): The name of the locator.

        Raises:
        None
        """
        locator_dict = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "css": By.CSS_SELECTOR,
            "xpath": By.XPATH,
            "link": By.LINK_TEXT,
            "partial_link": By.PARTIAL_LINK_TEXT,
            "tag": By.TAG_NAME,
        }
        locator_prefix = element.split('=')[0]
        locator_name = element.split('=')[1]
        if locator_prefix not in locator_dict.keys():
            self.logger("error", f"Element '{element}' with prefix '{locator_prefix}' is not valid locator.")
        return locator_dict[locator_prefix], locator_name

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
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
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
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(element))
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def take_screenshot(self, filename, element="tag=body"):
        """
        This function takes a screenshot of the web page and saves it in filename.

        Params:
            locator (string): Name of the element to take a screenshot of.
            filename (string): Name of the file to save the screenshot.

        Returns:
            None

        Raises:
            Exception: In case of any error.
        """
        locator = self.determine_locator(element)
        if self.username:
            user_path = os.path.join(self.test_dir, self.driver.name.capitalize(), self.username)
        else:
            user_path = os.path.join(self.test_dir, self.driver.name.capitalize())
        os.makedirs(user_path, exist_ok=True)
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(locator))
            self.driver.find_element(*locator).screenshot(os.path.join(user_path, filename))
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
        element = self.determine_locator(element)
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(element))
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
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(element))
            self.driver.find_element(*element).send_keys(text)
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def highlight(self, element):
        """
        This function highlights the given element on the web page.

        Args:
           element (tuple): The element to be highlighted.

        Returns:
           None

        Raises:
           Exception: If the element is not located on the page.
        """
        element = self.determine_locator(element)
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(element))
            self.driver.execute_script("arguments[0].style.border='5px solid red'",
                                       self.driver.find_element(*element))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def click(self, element):
        """
        Click on an element.

        Args:
            element (tuple): Tuple representing the element to be clicked

        Returns:
            None

        Raises:
            Exception: If element not found or if any exception occurs
        """
        element = self.determine_locator(element)
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(element))
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
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(element))
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
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e
