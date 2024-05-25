from common import *
from PIL import Image

def convert_to_file(input_file: str, output_file: str) -> None:
    # 1. Read pixels until red pixel is found
    pixels = read_pixels_until_eof(input_file)
    # 2. Map pixels to bits
    bits = map_pixels_to_bits(pixels)
    # 3. Convert groups of 8 bits into bytes
    bts = convert_bits_to_bytes(bits)
    # 4. Write the bytes to the file
    with open(output_file, "wb") as out_file:
        out_file.write(bts)


def read_pixels_until_eof(input_file: str) -> list[tuple]:
    img = Image.open(input_file)
     
    pixels = []
    for x in range(img.width):
        for y in range(img.height):
            pixel_data = img.getpixel((x, y))
            if pixel_data == EOF_RGB:
                return pixels
            pixels.append(pixel_data)

    return pixels
               

def map_pixels_to_bits(pixels: list[tuple]) -> list[int]:
    return [1 if pixel == BLACK_RGB else 0 for pixel in pixels]


def convert_bits_to_bytes(bits: list[int]) -> bytes:
    output = []
    bit_str_buff = ""
    for bit in bits:
        bit_str_buff += str(bit)
        if len(bit_str_buff) == 8:
            output.append(int(bit_str_buff, 2))
            bit_str_buff = ""
            
    return bytearray(output)