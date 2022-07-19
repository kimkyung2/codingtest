# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 13:57:36 2022

@author: kki
"""

# 15829번 Hashing
# 입력으로 들어오는 문자열은 영문 소문자로만 구성
# 영어알파벳에 순서대로 고유한 번호를 부여
# 하나의 문자열을 수열로 변환할 수 있음
# 해시 값을 계산하기 위해, 문자열 혹ㅇ느 수열을 하나의 정수로 치환
# H = l-1 시그마 i=0 airi modM
# r = 31, m = 1234567891

n = int(input())
string = input()
result = 0

for i in range(n):
    result += (ord(string[i]) - 96) * (31**i) # 아스키코드를 사용해서 계산하기 a = 97이므로 -96해주기 
    
print(result % 1234567891)
    