# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 10:38:48 2022

@author: kki
"""

# 1026번 보물
# 길이가 N인 정수 배열 A와 B가 있을때
# 함수 S를 정의하면 S = A[0] X B[0] +...+ A[n-1] X B[N-1]
# S의 값의 값을 가장 작게 만들기 위해 A의 수를 재배열하자
# 단, B에 있는 수는 재배열하면 안된다.
# S의 최솟값을 출력하는 프로그램 구현

#  s의 최솟값을 구하는 문제로 A 배열에서 제일 작은 수와 B 배열에서 제일 큰 수를 곱하고
# 그 다음으로 작은 수와 큰 수 곱하고 이런식으로 계속해서 더해주면 되는 문젲

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0

for i in range(n):
    s += min(a) * max(b)
    a.pop(a.index(min(a))) # a 배열에서의 최소값을 pop 함수를 이용해서 빼준다
    b.pop(b.index(max(b))) # b 배열에서의 최댓값을 pop함수를 이용해서 빼준다.


print(s)