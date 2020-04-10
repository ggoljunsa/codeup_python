# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:28:11 2020

@author: jangm
"""


n = int(input())

def printback(i):
    print(i)
    i -= 1
    if i<1:
        return
    printback(i)
    
printback(n)