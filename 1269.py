# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:36:43 2022

@author: kki
"""

# 1269번 대칭 차집합
# 자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다.
# 이 때, 두 집합의 대칭 차집합 원소의 개수를 출력하는 프로그램ㅇ르 작성하시오.
# 두 집합이 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.

n, m = map(int, input().split())

A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

print(len(A-B) + len(B-A))