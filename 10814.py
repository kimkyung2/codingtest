# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:21:55 2022

@author: kki
"""

# 10814번 나이순 정렬
# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
# 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는  프로그램 작성

# 파이썬은 기본으로 stable 정렬을 한다.
# stable정렬은 안정정렬로 입력받은 값들 중에 같은 값이 있는 경우 해당 값의 순서를 그대로 유지한다.
# unstable정렬에서는 위와 같은 정렬을 장담할 수 없다.

n = int(input())
member = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    
    member.append((age, name))
    
member.sort(key = lambda x : x[0]) # (age, name) 에서 age만 비교

for i in member:
    print(i[0], i[1])