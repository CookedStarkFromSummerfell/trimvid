import os.path

from main import trim_all

directory = str(input("Enter Directory Name: "))
input_folder = str(input("Enter Folder Name for input videos: "))
output_folder = str(input("Enter Folder Name for output videos: "))
clip_length = int(input("Enter Clip Length: "))

if directory is None or input_folder is None or output_folder is None or clip_length < 0:
    print("Invalid Inputs!")

input_path = os.path.join(directory, input_folder)
output_path = os.path.join(input_path, output_folder)

if not os.path.exists(output_path):
    os.makedirs(output_path)

trim_all(input_path, output_path, clip_length)
