# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 11:11:12 2022

@author: kki
"""

# 15903번 카드  합체 놀이
# 자연수가 써진 카드 n장을 갖고 있을 때 i번 카드에는 ai가 쓰여져 있음
# 카드 합체 과정
# 1) x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산(x=/=y)
# 2) 계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 씌움
# 합체를 총 m번 하면 놀이 끝
# m번의 합체를 끝낸 뒤, n장의 카드에 쓰여있는 수를 모두 더한 값이 이 놀이의 점수가 됨
# 점수를 가장 작게 만드는 것이 목표

n, m = map(int, input().split())
alist = list(map(int, input().split()))


for _ in range(m):
    alist.sort()

    sumlist = alist[0] + alist[1]
    alist[0] = sumlist
    alist[1] = sumlist
    
print(sum(alist))
    