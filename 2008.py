# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:01:31 2020

@author: jangm
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
"""


n = int(input())
m = input().split()
lowerFlag = True
upperFlag = True

for i in range(n):
    m[i] = int(m[i])

for i in range(n-1):
    if m[i] < m[i+1]:
        lowerFlag = False
    elif m[i] > m[i+1]:
        upperFlag = False

if upperFlag and lowerFlag:
    print("섞임")
elif upperFlag:
    print("오름차순")
elif lowerFlag:
    print("내림차순")
else:
    print("섞임")
    