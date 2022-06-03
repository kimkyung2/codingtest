# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:51:47 2022

@author: kki
"""

# 2562번 최댓값
# 9개의 서로 다른 자연수가 주어질 때,
# 이들 중 최댓값을 찾고 그 최댓값이 몇번째 수인지를 구하는 프로그램

n = []

for _ in range(9):
    a = int(input())
    n.append(a)
    
    
print(max(n))
print(n.index(max(n))+1)