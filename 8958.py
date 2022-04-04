# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:09:36 2022

@author: kki
"""

# 8958번 OX퀴즈
# OX퀴즈의 결과가 있다. O는 문제를 맏은 것이고, X는 문제를 틀린 것임.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 됨
# 애를 들어, 10번 문제의 점수는 3이 됨
# OOXXOXXOOO의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점
# OX의 결과가 주어졌을 떄, 점수를 구하는 프로그램 작성

T = int(input())

for _ in range(T):
    s = list(input())
    cnt = 0
    result = 0  # O를 입력받으면 합계가 올라감
    
    for i in s:
        if i == 'O':
            cnt += 1
            result += cnt
        elif i =='X':
            cnt = 0
            
    print(result)


    