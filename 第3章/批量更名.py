import os
path=r"H:\示例\第3章\批量更名"
for foldName, subfolders, filenames in os.walk(path):
    for filename in filenames:
            abspath=os.path.join(foldName,filename)
            extension =os.path.splitext(abspath)[1]
            new_name=filename.replace(extension,"2020"+extension)
            new_name="2020"+new_name
            os.rename(abspath,os.path.join(foldName,new_name))
