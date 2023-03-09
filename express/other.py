import json
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from express import utils


class Other:
    def __init__(self):
        self.test_dir = None
        self.password = None
        self.username = None

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
                    highlight_element = self.determine_locator(highlight_element)
                    # save the original style of the element
                    original_style = self.get_style(highlight_element)

                    self.highlight(highlight_element, style=highlight_style)
                    self.driver.save_screenshot(filepath)
                    self.remove_highlight(highlight_element, style=original_style)
                else:
                    self.driver.save_screenshot(filepath)
            else:
                if highlight and highlight_element:
                    highlight_element = self.determine_locator(highlight_element)
                    # save the original style of the element
                    original_style = self.get_style(highlight_element)

                    self.highlight(highlight_element, style=highlight_style)
                    self.driver.find_element(*element).screenshot(filepath)
                    self.remove_highlight(highlight_element, style=original_style)
                else:
                    element = self.determine_locator(element)
                    self.wait_for_element_visible(element)
                    self.driver.find_element(*element).screenshot(filepath)

            # annotate the screenshot
            if annotate_text:
                utils.annotate(filepath, annotate_text)
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
        try:
            self.type(username_locator, username)
            self.type(password_locator, password)
            self.click(submit)
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e
