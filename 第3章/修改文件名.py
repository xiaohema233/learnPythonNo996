import os
path=r"/Users/xiaohema/PycharmProjects/learnPythonNo996/第3章/case"
for foldName, subfolders, filenames in os.walk(path):    
    for filename in filenames: 
        abspath=os.path.join(foldName,filename)
        print(abspath)
        new_name=abspath.replace("\\","-").replace(":","-").replace("--","-")
        # new_name=abspath.replace("-","--").replace(":","--")
        print(new_name)
        os.rename(abspath,os.path.join(foldName,new_name))
