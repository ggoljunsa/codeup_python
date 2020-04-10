# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:38:36 2020

@author: jangm
"""


n = int(input())

def fact(i):
    if i==1:
        return 1
    else:
        return i*fact(i-1)
print(fact(n))
