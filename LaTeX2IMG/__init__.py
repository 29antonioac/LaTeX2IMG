"""
    LaTeX2IMG takes an expression, and name and an extension to convert that
    expression to a image file named "name.extension"
"""

import sys
import os
from urllib.parse import quote
from urllib.request import urlopen
from PIL import Image, ImageOps


def img2webp(path):
    """
    Takes a path of an image and converts it to webp
    """
    file, ext = os.path.splitext(path)
    image = Image.open(path).convert("RGBA")
    image = ImageOps.expand(image, 75)
    image.save(file + ".webp", "WEBP")
    os.remove(path)

def latex2img(expression, filename, extension):
    """
    Convert expression to an image called filename.extension
    """
    webp = False

    if extension not in ("gif", "png", "pdf", "swf", "emf", "svg", "webp"):
        print("Not supported extension, exiting...")
        sys.exit(-1)

    if extension == "webp":
        webp = True
        extension = "png"

    # Preparing text strings
    server = "http://latex.codecogs.com/" + extension + ".download?"
    fullname = filename + "." + extension
    size = "%5Cdpi%7B300%7D%20"

    # Quote expression
    expression = quote(expression)
    url = server + size + expression

    # Download file from url and save to output_file:
    with urlopen(url) as response, open(fullname, 'wb') as output_file:
        data = response.read()        # Un objeto "bytes"
        output_file.write(data)     # Se escribe en disco

    if webp:
        img2webp(fullname)
        extension = "webp"

    return filename + "." + extension
