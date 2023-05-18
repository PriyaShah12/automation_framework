from os import path
import os

def get_file(file_name):
    data_folder_path = "testData"
    data_folder_abs_path = os.path.abspath(data_folder_path)
    print("data_folder_abs_path -----> ", data_folder_abs_path)
    list_of_files = os.listdir(data_folder_abs_path)

    for file in list_of_files:
        print("File name in loop is--->", file)
        if file_name in file:
            print("****", path.join(data_folder_abs_path, file))
            filepath = path.join(data_folder_abs_path, file)
            myfilepath = os.path.abspath(filepath)
            print("File path is---->>>>", myfilepath)
            return myfilepath




