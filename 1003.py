# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:56 2022

@author: kki
"""

# 1003번 피보나치 함수
# 0의 개수 = 이전 1의 개수, 1의 개수 = 이전 0 + 이전 1개수

a = int(input())

for i in range(a):
    n = int(input())
    zero = [1, 0] # 0 호출횟수를 기억하는 리스트
    one = [0, 1] # 1 호출횟수를 기억하는 리스트
    
    for j in range(2, n+1):
        zero.append(zero[j-1] + zero[j-2]) # 이전 두 단계의 0 호출횟수를 더함
        one.append(one[j-1] + one[j-2])
    print("{} {}".format(zero[i], one[i]))
