import os

from express import identification, manipulation, navigation, other, utils, validation, waiting, _custom

"""
  Constants for the Actions class
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Actions(navigation.Navigation, waiting.Waiting, identification.Identification,
              manipulation.Manipulation, validation.Validation, other.Other, _custom.MyCustomActions):

    def __init__(self, driver, caplog):
        self.driver = driver
        self.caplog = caplog

        self.username = None
        self.password = None
        self.test_dir = None
        self.dir = BASE_DIR
        self.dir_in = os.path.join(BASE_DIR, 'in')
        self.dir_out = os.path.join(BASE_DIR, 'out')
