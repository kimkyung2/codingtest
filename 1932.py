# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 14:30:53 2022

@author: kki
"""

# 1932번 정수 삼각형
# 맨 위층부터 시작해서 아래에 있는 수 중 하나를 선ㄴ택하여 아래층으로 내려올 때,
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있음
# 삼각형의 크기는 1 이상 500이하, 각 수는 모두 정수이며, 범위는 0 이상 9999이하
# 다이나믹 프로그래밍이용

n = int(input())
dp = []

# 입력값을 이차원 리스트 형태로 dp 테이블에 저장하기
for i in range(n):
    dp.append(list(map(int,input().split())))
    
# 행을 기준으로 for문 구성
for i in range(1, n):
    # 열을 기준으로 for문 구성
    for j in range(0, i+1):
        if j == 0:
            dp[i][0] += dp[i-1][0] # 0 열끼리 더하기
        elif j == i: # 마지막 열끼리 더하기
            dp[i][j] += dp[i-1][j-1]
        else: # 두 화살 표 중 더 큰 경우 받아 들이기
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
            
            
print(max(dp[n-1])) # n-1행에서의 최댓값 출력