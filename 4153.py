# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:45:52 2022

@author: kki
"""

# 4153번 직각삼각형
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하기
# 직각삼각형이면 right 아니면 wrong 출력

def map_():
    while True:
        H, A, B = map(int,input().split())
        
        if H==0 or A ==0 or B ==0:
            break
        
        H *= H
        A *= A
        B *= B
        
        if H+A == B or H+B == A or B+A ==H:
            print('right')
        else:
            print('wrong')

map_()            
# list 사용하는 방법
def list_():
    while True:
        num = list(map(int, input().split()))
        
        max_num = max(num) # list에서 가장 큰 값을 받아놓기
        
        if sum(num) == 0: # list의 값들이 0이면 while문을 빠져나온다
            break
        
        num.remove(max_num) # list에서 가장 큰 값을 빼줌
        
        if num[0]**2 + num[1]**2 == max_num**2: # 피타고라스의 정리를 이용해서 직각삼각형이 맞다면 right 출력 아니면 wrong 출력
            print('right')
        else:
            print('wrong')
list_()