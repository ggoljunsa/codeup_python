# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:31:05 2020

@author: jangm
"""


x, y = map(int, input().split())

def printeven(a, b):
    if a>b:
        return
    if a%2 ==1:
        print(a, end = ' ')
    a+=1
    printeven(a, b)
    
printeven(x, y)
