# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 10:27:05 2022

@author: kki
"""
# 1075번 나누기
# 정수 N의 가장 뒤 두자리를 바꿔, N을 F로 나누어 떨어지게 만들기
# 가능한 수가 여러 가지이면, 뒤 두 자리를 가장 작게 만들기
# 100 <= N <=2,000,000,000 , F <= 100

# 풀이
# 1. N의 맨 뒷자리 2개는 필요없는 숫자로 '00'으로 만든 후 1씩 증가
# 2. F값으로 나누어 떨어질 때까지 비교

n = input()
f = int(input())
temp = int(n[:-2]+'00')

while True:
    if temp % f == 0:
        break
    temp += 1
    
print(str(temp)[-2:])