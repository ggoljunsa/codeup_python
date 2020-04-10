# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:33:05 2020

@author: jangm
"""


m = []

n = int(input())

for i in range(n):
    m.append([])
    for j in range(n):
        m[i].append(0)

k = int(1)

for i in range(n):
    for j in range(n):
        m[j][i] = k
        k = k+1

for i in range(n):
    for j in range(n):
        print('%d' %m[i][j], end = ' ')
    print()