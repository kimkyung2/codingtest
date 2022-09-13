# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:31:41 2022

@author: kki
"""

# 5073번 삼각형과 세 변
# 삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의
# Equilateral : 세변의 길이가 모두 같은 경우
# Isosceles : 두변의 길이만 같은 경우
# Scalene : 세변의 길이가 모두 다른 경우
# 단 주어진 세변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 Invalid를 출력


while True:
    data = list(map(int, input().split()))
    
    if data[0] == data[1] == data[2] == 0: # 종료조건
        break
    
    data.sort(reverse = True) # 삼각형의 조건을 알기 위해서는 입력 받은 data 크기를 알아야함
    
    if data[0] >= data[1] + data[2]: # 삼각형의 조건 : 가장 긴 변의 길이가 다른 두변의 길이의 합보다 작으면 성립
        print("Invalid")

    else:
        if data[0] == data[1] == data[2]: # 세변의 길이가 모두 같은 경우
            print("Equilateral")
        elif data[0] == data[1] or data[1] == data[2] or data[2] == data[0]: # 두 변의 길이만 같은 경우
            print("Isosceles")
        else :  # 세변의 길이가 모두 다른 경우
            print("Scalene")
    