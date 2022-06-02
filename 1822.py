# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 13:49:29 2022

@author: kki
"""

# 1822번 차집합
# 몇 개의 자연수로 이루어진 두 집합 A와 B가 있음
# 집합 A에는 속하면서 집합 B에는 속하지 않는 모든 원소를 구하는 프로그램 작성

a, b = map(int, input().split())

A, B = {}, {}

for n in map(int, input().split()):
    A[n] = 1
    
    
for n in map(int, input().split()):
    B[n] = 1
    

# 리스트로 풀면 시간초과가 나지만 해쉬로 풀면 문젲 해결 가능
C = []

for i in A:
    if i not in B:
        C += [i]
        
print(len(C))
print(*sorted(C))

# 리스트로 반복문을 돌면 시간초과가 나지만 딕셔너리로 돌면 시간초과가 발생하지 않음
# 이유는 딕셔너리의 대부분 연산의 시간 복잡도는 O(1)이며 특히 위의 if i not in B: 구문에서 리스트와 시간차이가 발생