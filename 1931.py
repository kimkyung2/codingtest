# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:28:28 2022

@author: kki
"""
# 사용하고자 하는 n개의 회의에 대하여 회의실 사용표를 드려고 함.
# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고,
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대 개수를 찾기
# 회의는 한번 시작하면 중간에 중단 할 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있음
# 회의의 시작시간과 끝나는 시간이 같을 수도 있음.

n = int(input())
time = []

for _ in range(n):
    first, second = map(int, input().split())
    time.append([first, second])

time = sorted(time, key=lambda x: x[0]) # 시작하는 시간으로 정렬
time = sorted(time, key=lambda x: x[1]) # 끝나는 시간으로 정렬

last = 0 # 회의의 마지막 시가능ㄹ 저장할 변수
count = 0  # 회의 개수를 저장할 변수

for i, j in time:
    if i>= last:
        count += 1
        last =j
print(count)