import os

from express import _identification

"""
  Constants for the Actions class
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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

    from express._identification import find_nearest_xpath

    from express._manipulation import click, hover, move_mouse_to_element, move_mouse_to, \
        drag_and_drop, type, remove_highlight, highlight

    from express._navigation import go, scroll_into_element, scroll_to_bottom_page, \
        scroll_to_top_page, switch_to_iframe, switch_to_default_content

    from express._other import prepare_tests, set_credentials, take_screenshot, load_json, login

    from express._validation import validate_style, get_style
    from express._waiting import wait_for_element_selected, wait_between, \
        wait_for_element_attribute, wait_for_element_presence, wait_for_element_clickable, wait_for_page_to_load
