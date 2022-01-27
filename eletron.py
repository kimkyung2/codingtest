# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:24:32 2022

@author: kki
"""

# 1076번 저항
# 저항은 색 3개 이용해서 몇 옴인지 나타냄, 처음 색 2개는 저항의 값, 마지막 색은 곱하는 값
# ex) yellow, violet, red --> 4700
# 풀이
# 색의 값은 배열의 순서와 똑같고, 곱하는 값은 10의 거듭제곱과 같다


# 저항의 값들을 딕셔너리로 구성
color = {
    'balck':0, 
    'brown':1, 
    'red':2, 
    'orange':3, 
    'yellow':4, 
    'green':5, 
    'blue':6, 
    'violet':7, 
    'grey':8, 
    'white':9
 }

A = input()
B = input()
C = input()

ans = (color[A]*10 + color[B] ) * (10 ** color[C])
print(ans)