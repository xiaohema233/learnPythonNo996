# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:06:35 2020

@author: Administrator
"""

import pytesseract as pt
from PIL import Image
img = Image.open("扫描版PDF_文字.jpeg")
text = pt.image_to_string(img,lang='chi_sim')
print(text)


