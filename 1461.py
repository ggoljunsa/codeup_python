# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:33:41 2020

@author: jangm
"""

a, r, n = map(int, input().split())

for i in range(1, n):
    a = a*r
print(a)