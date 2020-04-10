# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:41:04 2020

@author: jangm
"""


n, m = map(int, input().split())

i = int(1)
a = []

for i in range(n+1):
    a.append([])
    for j in range(m+1):
        a[i].append(0)

x, y = 0, 1

while i <= n*m:
    while x<=n:
        x = x+1
        a[y][x] = i
        i = i+1
    while y<=m:
        y = y+1
        a[y][x] = i
        i = i+1
    while x>=1:
        x = x-1
        a[y][x] = i
        i = i+1
    while y>=1:
        y = y -1
        a[y][x] = i
        i = i+1
