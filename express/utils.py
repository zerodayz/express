import json
import os

from PIL import Image, ImageFont, ImageDraw


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


def load_json(filename):
    """
    This function loads a JSON file and returns the data.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        dict: The data from the JSON file.

    Raises:
        Exception: If there is an error loading the JSON file.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    try:
        with open(os.path.join(base_dir, 'in', filename)) as f:
            return json.load(f)
    except Exception as e:
        print("Error: ", e)
        raise e
