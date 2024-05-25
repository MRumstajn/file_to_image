from PIL import Image
import math
from common import *

def convert_to_img(file: str, output_image: str):
    # read file data
    with open(file, "rb") as fl:
        raw_data = fl.read()

    output_bits = convert_bytes_to_bits_array(raw_data)

    pixels = map_bits_to_pixels(output_bits)

    generate_image(pixels, output_image)
    

def calculate_image_size(pixel_count: int) -> tuple[int, int]:
    width = math.isqrt(pixel_count)
    height = width

    if width * height < pixel_count:
        height += 1

    if width * height < pixel_count:
        width += 1

    return (width, height)


def map_bits_to_pixels(bits: list[int]) -> list[tuple]:
    # map bits to black and white pixels.
    # Array of tuples where each tuple is a pixel (RGB value).
    pixels = []
    for bit in bits:
        pixels.append(BLACK_RGB if bit == 1 else WHITE_RGB)

    return pixels


def convert_bytes_to_bits_array(raw_data: bytes) -> list[int]:
    output_bits = []
    for byt in raw_data:
        bit_str = "{0:b}".format(byt)
       
        buff = []
        for str_bit in bit_str:
            buff.append(1 if str_bit == "1" else 0)

        required_padding = 8 - len(bit_str)
        for _ in range(required_padding):
            buff.insert(0, 0)

        for bit in buff:
            output_bits.append(bit)
        
    return output_bits


def generate_image(pixels: list[tuple], output_image: str) -> None:
    width, height = calculate_image_size(len(pixels))
    img  = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            if len(pixels) == 0:
                img.putpixel((x, y), EOF_RGB)
            else:
                img.putpixel((x, y), pixels.pop(0))
    
    img.save(output_image)