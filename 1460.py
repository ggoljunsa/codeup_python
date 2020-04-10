# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:15:17 2020

@author: jangm
"""


x = input()
n = int(x)
m = []
k=1
for i in range(n):
    m.append([])
    for j in range(n):
        m[i].append(k)
        k = k+1    
for i in range(n):
    for j in range(n):
        print(m[i][j], end = ' ')
    print()