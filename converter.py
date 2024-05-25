import os
import numpy
from PIL import Image

def convert_to_img(file: str):
    # get size
    size_in_bytes = os.path.getsize(file)
    size_in_bits = 8 * size_in_bytes

    # generate image

