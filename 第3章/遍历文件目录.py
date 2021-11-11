import os
path=r"/Users/xiaohema/PycharmProjects/learnPythonNo996/第3章/"
for foldName, subfolders, filenames in os.walk(path):
    for filename in filenames:
            print(foldName,filename)
