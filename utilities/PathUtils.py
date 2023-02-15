from os import path
import os


def get_file(file_name):
    data_folder_path = "testData"

    data_folder_abs_path = path.join(path.abspath(path.curdir), data_folder_path)

    print("data_folder_abs_path -----> ", data_folder_abs_path)

    list_of_files = os.listdir(data_folder_abs_path)
    for file in list_of_files:
        print("File name in loop is--->", file)
        if file_name+".xlsx" in file:
            print("File Found ->", file)
            return path.join(data_folder_abs_path, file)


#get_file("test_login_ddt")


