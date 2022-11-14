# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:33:23 2022

@author: kki
"""

# 2166번 다각형의 면적
# 2차원 평면상에 N개의 점으로 이루어진 다각형이 있다.
# 이 다각형의 면적을 구하는 프로그램을 작성하시오.


n = int(input())

x, y, = [], []

for i in range(n):
    a, b = map(int, input().split())
    x.append(a), y.append(b)
x.append(x[0]), y.append(y[0])

xr, yr = 0, 0

for i in range(n):
    xr += x[i] * y[i+1]
    yr += y[i] * x[i+1]
    
print(round(abs((xr-yr)/2),1))
    