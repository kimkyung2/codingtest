# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 10:30:10 2022

@author: kki
"""

# 1149번 RGB거리
# 집이 n개가 있을 때, 집을 빨강, 초록, 파랑 중 하나의 색으로 칠해야 함
# 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때,
# 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값 구하기
# 구칙
# 1. 1번 집의 색은 2번 집의 색과 같지 않아야 함
# 2. n번 집의 색은 n-1번의 색과 같지 않아야 함
# 3. i(2 <= i <= n-1)번 집의 색은 i-1번 ,i+1번 집의 색과 같지 않아야 함

n = int(input())
color = []


for _ in range(n):
    color.append(list(map(int, input().split())))
    
for i in range(1, len(color)):
    # 첫번째 배열로 보지말고 두번째 배열로 시작해서 결과 구하기, color[][0] = Red, color[][1] = green, color[][2] = blue 
    color[i][0] = min(color[i-1][1], color[i-1][2]) + color[i][0] 
    # 두번째 배열중 R을 선택했을 때, 첫번째 배열은 G과 B중 최소값을 선택하여 더하기
    color[i][1] = min(color[i-1][0], color[i-1][2]) + color[i][1]
    color[i][2] = min(color[i-1][0], color[i-1][1]) + color[i][2]
    
print(min(color[n-1])) # 배열은 0부터 시작이니까 n값에다가 -1 해주기, color[n-1]까지의 값 중 최소값 출