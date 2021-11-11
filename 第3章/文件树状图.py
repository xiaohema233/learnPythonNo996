import os
def filetree(path, depth):
    if depth == 0:
        print("文件夹:" + path)
    for file in os.listdir(path):
        print("|    " * depth + "+--" + file)
        directory = path +'/'+ file
        if os.path.isdir(directory):
            filetree(directory, depth +1)
filetree(r'H:\示例\第3章\case', 0)
