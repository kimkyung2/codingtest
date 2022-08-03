# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 14:22:59 2022

@author: kki
"""

# 2164번 카드

# n장의 카드에 순서대호 번호가 부여되고, 1번 카드가 제일 위에, n번 카드가 제일 아래인 순서대로 카드가 놓여있다.
# 다음 동작을 카드가 한 장 남을 때까지 반복하게 된다.
# 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 젱리 아래에 있는 카드 밑으로 옮긴다.
# n이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성

from collections import deque

n = int(input())
q = deque()

for i in range(1, n+1):
    q.append(i)
    
while True:
    if len(q) == 1:
        print(q[0])
        break
        
    q.popleft()
    q.append(q.popleft())