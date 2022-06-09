# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 10:29:26 2022

@author: kki
"""

# 1449번 수리공 항승
# 파이프에서 물이 새는 곳은 가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다
# 길이가 L인 테이프를 무한개 가지고 있다.
# 테이프를 이용해서 물을 막을 때, 적어도 그 위치의 좌우 0.5만큼 간격을 줘야된다고 생각함
# 물이 새는 곳의 위치와 항승이가 가지고 있는 테이프 길이 L이 주어졌을 때
# 항승이가 필요한 테이프의 최소 개수를 구하는  프로그램
# 테이프는 자를 수 없고, 테이프를 겹쳐서 붙이는 것도 가능

N, L = map(int, input().split()) # N : 물이 새는 곳의 개수, L : 테이프의 길이 

water = list(map(int, input().split())) # 물이 새는 곳의 위치

water.sort() # 물이 새는 위치를 오름차순 함

start = water[0] # 테이프를 처음 붙이는 시작점
cnt = 1 # 필요한 테이프 개수

for i in water:
    length = start + L -1
    if i <= length:
        continue
    else:
        cnt += 1
        start = i

print(cnt)