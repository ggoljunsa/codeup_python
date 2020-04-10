# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:45:49 2020

@author: jangm
"""


a, b = map(int, input().split())
if a>b:
    a, b = b, a
for i in range(a, b+1):
    print('%d' %i, end = ' ')
    