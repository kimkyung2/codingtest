# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:40:42 2022

@author: kki
"""

# 1043번 거짓말
# 지민이가 간 파티의 사람 수는 N명이다. 이 때 지민이가 할 이야기의 진실을 아는 사람이 주어짐
# 파티에 오는 사람들의 번호가 주어질 때, 지민이는 모든 파티에 참가해야함
# 지민이가 과장된 이야기를 할 수 있는 파티 개수의 최댓값 구하기

# 조건 
# 사람 수 : N, 파티의 수 : M
# 이야기의 진실을 아는 사람 수와 번호 주어짐
# 각 파티마다 오는 사람의 수와 번호가 주어짐

# 풀이
# 해결하기 위해 거짓말을 하면 안 될 사람들을 찾고, 그 사람들 전부가 안 오는 파티의 수를 알아내면 됨
# 거짓말을 하면 안될 사람: 이미 진실을 알고있는 사람과 그 사람들과 같은 파티에 참석한 사람들(진실을 알게될 사람) 

n, m = map(int, input().split())
trues = set(list(map(int, input().split()))[1:])
party = [] 
cnt = [] 

# party = 각 파티의 구성원을 집어넣음
for _ in range(m):
    data = set(map(int, input().split()[1:]))
    if data:
        party.append(data)
        cnt.append(1) # 파티의 수만큼 원소를 만들어주고 , 각 값을 1로 둠
        
for _ in range(m):  # 파티의 수만큼 각 party의 번호와 구성원을 뽑아 반복문을 돌림
    for i, p in enumerate(party): # enumerate() : 리스트를 순회하면서 리스트의 각 원소의 인덱스와 원소를 반환함
        if trues & p: #파티의 구성원과 진실을 아는 사람들 간에 교집합이 존재한다면, cnt 리스트의 해당 번호에 해당하는 값을 0으로 변경
            cnt[i] = 0  # 파티원을 진실을 알고 있는 사람들이 저장되어 있는 set() 자료형에 update 시켜줌, update와 |= 이 둘은 같은 효과를 봄
            trues |= p
            
print(sum(cnt)) # cnt 리스트의 합을 구해 출력


































