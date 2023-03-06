import os

from PIL import Image, ImageFont, ImageDraw


def annotate(image, text):
    img = Image.open(image)
    font = ImageFont.load_default()
    img_editable = ImageDraw.Draw(img)
    img_editable.text((15, 15), text, (255, 0, 0), font=font)
    img.save(image)
