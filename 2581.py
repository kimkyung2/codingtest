# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:38:34 2022

@author: kki
"""

# 2581번 소수
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 소수의 합과 최솟값을 찾는 프로그램
# M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개 있으므로
# 소수의 합은 620이고 최솟값은 61이 됨
# 단, M이상 N이하의 자연수 중 소수가 없을 경우 첫째 줄에 -1을 출력
# 입력 첫째줄에 M, 둘째줄에 N이 주어짐

M = int(input())
N = int(input())

arr = [] # 소수들 담을 리스트

for i in range(M, N+1):
    err = 0
    if i > 1:
        for j in range(2, i):
            if i%j == 0:
                err += 1
                break # 2 부터 i까지 나눈 몫이 0이면 err 증가하고 for문 끝냄
        if err == 0:
            arr.append(i) # err가 없다면 리스트에 추가

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)