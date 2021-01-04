"""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
"""

n = int(input())

m = []
m = input().split(" ")

upperFlag = True
lowerFlag = True

for i in range(n-1):
    if int(m[i])<int(m[i+1]) :
        lowerFlag = False
        
    if int(m[i])>int(m[i+1]):
        upperFlag = False
        
if upperFlag == True:
    print("오름차순")
elif lowerFlag == True:
    print("내림차순")
else:
    print("섞임")