# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:51:44 2022

@author: kki
"""
# 1085번 직사각형에서 탈출
# 한수 현위치(x,y) 이고 직사각형의 왼족 아래 꼭짓점은 (0,0) , 오른쪽 위 꼭짓점은 (w, h)
# 직사각형의 경계선까지 가는 거리의 최솟값 구하기

# 풀이
# 직사각형 안에 있는 한 점에서 경계까지의 길이의 최솟값을 구하는 것으로
# 총 4개의 길이가 나온다
# 4개의 길이를 구하는 방법은 x와 y의 길이 2개와 w,h의 길이에 x,y의 값을 뺀 수 2개가 있다.
# 이 4개의 길이를 비교하여 최솟값을 구하면 된다.

# x = int(input())
# y = int(input())
# w = int(input())
# h = int(input())

x, y, w, h = map(int, input().split())

print(min(x, y, w-x, h-y))