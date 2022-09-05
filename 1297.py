# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 16:46:45 2022

@author: kki
"""

# 1297번 TV 크기
# TV의 대각선 길이와 높이 너비의 비율이 주어졌을 때, 실제 높이와 너비의 길이를 출력하는 프로그램 작성


D, H, W = map(int, input().split())

r = D/(H**2 + W**2)**0.5

h = r * H
w = r * W

print(int(h), int(w))