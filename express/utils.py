import os
import random
import time

from PIL import Image, ImageFont, ImageDraw
from selenium.webdriver.common.by import By


def annotate(image, text, color=(255, 0, 0), size=64):
    img = Image.open(image)
    # get the size of the image
    width, height = img.size
    # position the text above the bottom left corner
    position = (15, height - 15 - size)
    current_dir = os.path.dirname(os.path.realpath(__file__))
    font_path = os.path.join(current_dir, 'fonts', 'Roboto-Regular.ttf')
    font = ImageFont.truetype(font_path, size=size)
    img_editable = ImageDraw.Draw(img)
    img_editable.text(position, text, color, font=font)
    img.save(image)


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

