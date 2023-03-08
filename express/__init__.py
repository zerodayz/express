import os

from express import identification, manipulation, navigation, other, utils, validation, waiting

"""
  Constants for the Actions class
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Actions(navigation.Base, waiting.Base, identification.Base, manipulation.Base, validation.Base, other.Base):

    def __init__(self, driver, caplog):
        self.driver = driver
        self.caplog = caplog

        self.username = None
        self.password = None
        self.test_dir = None
        self.dir = BASE_DIR
        self.dir_in = os.path.join(BASE_DIR, 'in')
        self.dir_out = os.path.join(BASE_DIR, 'out')
