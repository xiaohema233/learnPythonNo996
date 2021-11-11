import os,shutil,hashlib
path=r"H:\示例\第3章\case"
list=[]
for file in os.listdir(path):
    fileName = path +'\\'+ file
    if os.path.isdir(fileName):
        shutil.rmtree(fileName)
    else:
        m = hashlib.md5() 
        with open(fileName, "rb") as mfile:
            m.update(mfile.read()) 
        md5_value = m.hexdigest() 
        if md5_value in list: 
            os.unlink(fileName)
        else:
            list.append(md5_value)
