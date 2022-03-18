# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:03:08 2022

@author: kki
"""

# 1717번 집합의 표현
# n+1개의 집합을 이루고 있을 때,
# 여기에 합집합 연산과 두 원소가 같은 집합이 포함되어 있는지를 확인하는 연산을 수행

# 첫째 줄 n과 m이 주어짐
# m은 입력으로 주어지는 연산의 개수
# m개의 줄에는 각각의 연산이 주어짐.
# 합집합은 0 a b 의 형태로 입력이 주어짐
# a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미
# 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어짐
# a와 b는 n 이하의 자연수 또는 0이며 같을 수도 있음


# union-find 알고리즘 사용하여 풀기
# find : 노드 x가 어느 집합에 포함되어 있는지 찾는 연산
# union : 노드 x가 포함된 집합과 노드 y가 포함된 집합을 합치는 연산

n, m = map(int, input().split())
parent = []
# parnet 초기화
for i in range(n+1): # parent[]를 작성하여 i노드의 부모노드라고 정의하고 초기화해줌
    parent.append(i) # parent[i] = i 이면 루트노드
    
# find 함수
# def find(x):
#     if parent[x] == x: # parent[x] = x이면 x가 루트노드이므로 return x 해주고, 
#         return x 
#     return find(parent(x))  # 아니면 재귀적으로 연산하여 루트노드를 return 해줌
# 이렇게 구현할 수 있는데 이러면 문제가 발생함
# 한쪽으로 치우쳐진 tree가 있을 경우, find 함수가 루트 노드를 찾는데 O(N)의 시간 복잡도를 가짐, tree 구현 이점이 사라진다.

# find 함수 개선
def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return p
    
def union(x, y): # x, y 두개의 값을 받아 두 노드가 포함되어 있는 집합을 합쳐줌
    x = find(x) # find를 통해 각각의 루트를 찾아준 후
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for _ in range(m):        
    operation, a, b = map(int, input().split())
    if operation == 0:
        union(a, b)
    elif operation == 1:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')