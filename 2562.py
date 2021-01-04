# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 00:58:26 2020

@author: jangm
"""


def h(a, b):
    r = b
    n = a+r-1
    
    if r<0:
        return 0
    c1 = 1
    c2 = 1
    
    for i in range(n-r+1, n+1):
        c1 = c1*i
    for i in range(1, r+1):
        c2 = c2*i
    return int(c1/c2)

n, k = input().split()
n = int(n)
k = int(k)

if k == 1:
    print(n)
else:
    m = k+1
    o = n-2*k+1
    
    print(h(m, o))