# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:34:58 2023

@author: kki
"""

# 5347번 LCM
# 두 수 a 와 b가 주어졌을 때, a와 b의 최소 공배수를 구하는 프로그램을 작성


# from math import gcd

# def lcm(x, y):
#     return x*y// gcd(x, y)    #최대 공약수

# a와 b의 최소 공배수를 구하는 방법은 a와 b를 곱하고 a와 b의 최대 공약수를 나누는 방법
# 따라서 최대 공약수를 구하는 gcd 함수를 정의 : 유클리드 호제법을 이용함


def gcd(a, b):
    while b:
        mod = b
        b = a% b
        a = mod
    return a


n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(a*b // gcd(a, b))
    