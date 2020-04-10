# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:00:05 2020

@author: jangm
"""


m = []
n, k = map(int, input().split())

for i in range(2*n):
    m.append([])
    for j in range(2*n):
        m[i].append(' ')
        
for i in range(n):
    m[i][0] = '*'
    m[0][i] = '*'
    m[i][n-1]= '*'
    m[n-1][i]= '*'
    
for i in range(2*n):
    for j in range(2*n):
        if (j+i+1)%3 == 0:
            m[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(m[i][j], end = '')
    print()