# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:36:13 2020

@author: jangm
"""

import cv2
from PIL import ImageGrab
import numpy as np


while True:
    img = ImageGrab.grab()
    cv2.imshow("windows", img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()
