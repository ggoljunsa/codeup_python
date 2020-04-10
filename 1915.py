# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:55:47 2020

@author: jangm
"""

n = int(input())
m = []
for i in range(21):
    m.append(0)
m[1] = 1
m[2] = 1

def fibo(n):
    if m[n]==0:
        m[n] = fibo(n-1)+fibo(n-2)
    return m[n]

print(fibo(n))