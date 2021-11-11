# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:55:52 2020

@author: Administrator
"""
import compoundfiles
from struct import unpack
file=r"H:\示例\第6章\格式研究\HelloWorld.doc"
reader = compoundfiles.CompoundFileReader(file)
wordDocument= reader.open("WordDocument").read()
fcClx  = unpack("L", wordDocument[418:422])[0]
lcbClx = unpack("L", wordDocument[422:426])[0]
table = reader.open('1Table').read()
clx = table[fcClx:fcClx+lcbClx]
lcb = unpack("l", clx[1:5])[0]
PlcPcd = clx[5:5+lcb]
num_Pcd=int((lcb-4)/12)
aPcd = PlcPcd[8:16]
FcCompressed  = unpack("L", aPcd[2:6])[0]
fCompressed = (FcCompressed  & 0x40000000) == 0x40000000
if fCompressed==True:
    encode="Windows-1252"
else:
    encode="UTF-16"
fc = FcCompressed & 0x3FFFFFFF
size = unpack("l", PlcPcd[4:8])[0]-unpack("l", PlcPcd[0:4])[0]
if fCompressed==True:
    size=size
    fc=int(fc/2)
else:
    size=size*2
    fc=fc
print(wordDocument[fc:fc+size].decode(encode))

