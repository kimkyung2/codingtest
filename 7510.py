# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 11:21:17 2022

@author: kki
"""

# 7510번 고급 수학
# 줄자를 이용해 삼각형 세변의 길이를 측정한 다음, 직각 삼각형인지 아닌지를 알아보려고함.
# 삼각형 세변의 길이가 주어졌을 때, 직각 삼가곃ㅇ인지 아닌지를 구하는 프로그램을 작성

t = int(input())

for i in range(t):
    li = list(map(int,input().split()))
    li.sort()

    
    if li[0]**2 + li[1]**2 == li[2]**2:
        print(f"Scenario #{i+1}:")
        print("yes\n")
    
    else:
        print(f"Scenario #{i+1}:")
        print("no\n")
    
    
    
    
    
    
    
    