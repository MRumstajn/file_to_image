from converter import convert_to_img

inp_file = input("File name: ")
convert_to_img("files/" + inp_file, "output/" + inp_file + ".png")