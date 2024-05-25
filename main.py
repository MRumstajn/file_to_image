from encoder import convert_to_img
from decoder import convert_to_file

mode = input("Mode (E/D): ")
inp_file = input("File name: ")

if mode.lower() == "e":
    convert_to_img("files/" + inp_file, "output/" + inp_file + ".png")
else:
    convert_to_file("output/" + inp_file, "files/" + inp_file.removesuffix(".png"))