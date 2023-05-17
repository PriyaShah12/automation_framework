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
            # return path.join(data_folder_abs_path, file)
            filepath = path.join(data_folder_abs_path, file)
            myfilepath = os.path.abspath(filepath)
            print("File path is---->>>>", myfilepath)
            return myfilepath

# def get_file(file_name):
#     data_folder_path = "testData"
#     data_folder_abs_path = os.path.relpath(data_folder_path, start=os.defpath)
#     print("data_folder_abs_path -----> ", data_folder_abs_path)
#     list_of_files = os.listdir(data_folder_abs_path)
#
#     for file in list_of_files:
#         print("File name in loop is--->", file)
#         if file_name in file:
#             print("****", path.join(data_folder_abs_path, file))
#             # return path.join(data_folder_abs_path, file)
#             filepath = path.join(data_folder_abs_path, file)
#             myfilepath = os.path.abspath(f".\\..\\automation_framework\\{filepath}")
#             print("File path is---->>>>", myfilepath)
#             return myfilepath




#get_file("test_login_ddt") #it will not print correct path here as we are calling
#from current dir and our method is in other dir, thats why we need defpath



