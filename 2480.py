# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:31:24 2022

@author: kki
"""

# 24880번 주사위 세개
# 1~6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있음
# 1. 같은 눈이 3개가 나오면 10,000원 + (같은 눈) x 1000원의 상금을 받음
# 2. 같은 눈이 2갬나 나오는 경우에는 1,000원 + (같은 눈) x 100원의 상금을 받음
# 3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈) x 100원의 상금을 받게 됨

a, b, c = map(int, input().split())

if a == b and b == c and a == c:
    print( 10000 +(a*1000)) 
elif a == b or a == c:
    print(1000 + (a*100))
elif b == c:
    print(1000 + (b*100))
else:
    print(100*max(a,b,c))