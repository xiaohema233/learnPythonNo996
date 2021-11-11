# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:06:35 2020

@author: Administrator
"""

import cv2
import numpy as np
from PIL import Image
img_path = r'H:\示例\第9章\9-E.jpg'
img = cv2.imdecode(np.fromfile(img_path,dtype = np.uint8),-1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.where((gray<200),gray,255)
Image.fromarray(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
file_path= r'H:\示例\第9章\watermark_removed.png'
cv2.imencode('.png', gray)[1].tofile(file_path)

