# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 11:40:13 2022

@author: kki
"""

# 11053번
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성
# 예를들어) 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 
# A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

n = int(input())
a = list(map(int, input().split()))

# dp 리스트에 자신을 포함하여 만들 수 있는 부분 수열 크기를 저장
dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        # 현재 위치(i)가 이전에 있는 원소(j)가 큰지를 확인
        # 크다면, 그 위치의 dp 값에 1을 더해주면 됨(단, 현재 위치의 dp[i]가 dp[j]보다 작은 경우에만 적용함)
        if a[i] > a [j] and dp[i] < dp[j]:
            dp[i] = dp[j]
            
    dp[i] += 1
    
# 마지막에 dp에 있는 값 중 max를 출력    
print(max(dp))