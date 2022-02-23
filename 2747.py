# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 12:07:35 2022

@author: kki
"""

# 2747번 피보나치 수
# 피보나치 수는 0과 1로 시작함
# 피보나치 수의 식 Fn = F(n-1) + F(n-2) (n>=2)
# n이 주어졌을 떄, n번째 피보나치 수를 구하시오

n = int(input())
p = [0, 1]

for i in range(2, n+1):
    p.append(p[i-1] + p[i-2])
    
print(p[n])
    