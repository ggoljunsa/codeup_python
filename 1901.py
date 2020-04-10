# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:17:51 2020

@author: jangm
"""

import sys
sys.setrecursionlimit(10000)

n = input()

def f(i):
    if i>int(n):
        return
    print(i)
    i+=1
    f(i)

f(1)