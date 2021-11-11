import os,shutil
path=r"H:\示例\第3章\case"
for file in os.listdir(path):
    directory = path +'\\'+ file
    if os.path.isdir(directory):
            shutil.rmtree(directory)
