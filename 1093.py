# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:43:14 2020

@author: jangm
"""

n = int(input())
m = list(input().split())

for i in range(n):
    print(m[n-i-1], end = ' ')
