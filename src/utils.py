import os
from PIL import Image, ImageFont, ImageDraw


def annotate(image, text, position=(15, 15), color=(255, 0, 0), size=64):
    img = Image.open(image)
    current_dir = os.path.dirname(os.path.realpath(__file__))
    font_path = os.path.join(current_dir, 'fonts', 'Roboto-Regular.ttf')
    font = ImageFont.truetype(font_path, size=size)
    img_editable = ImageDraw.Draw(img)
    img_editable.text(position, text, color, font=font)
    img.save(image)
