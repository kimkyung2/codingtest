# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:58:34 2022

@author: kki
"""

# 9372번 상근이의 여행
# 상근이가 최대한 적은 종류의 비행기를 타고 국가들을 이동하려 한다.
# 이번 방학 동안의 비행 스케줄이 주어졌을 때, 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 도와주자.
# 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐 가도 된다.


# 신장 트리를 이용한 방법
# 주어진 비행 스케줄은 항상 연결 그래프를 이룸
# 따라서 아무 노드나 선택해도 그 노드에서 모든 노드로 갈 수 있음을 의미
# 연결 그래프를 유지하기 위한 간선의 최소 개수는 (노드의 수 -1)
# 이를 신장 트리라 한다.
# 즉, 비행기의 종류 = 간선 수
# 여행 갈 나라의 수 = 노드의 수
# 간선의 최소 수 = 노드의 수 -1

# T = int(input())

# for _ in range(T):
#     n, m = map(int, input().split())
#     for _ in range(m):
#         a, b = map(int, input().split())
#         # input() # 무조건 연결그래프이므로 입력 값을 무시해도 됨
#     print(n-1)

# bfs를 이용한 방법

def dfs(node, cnt):
    # 방문
    check[node] = 1
    for n in graph[node]:
        if check[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    
    # 각 노드가 연결된 정보를 표현
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # 각 노드의 방문유무
    check = [0]*(n+1)
    check[1] = 0
    result = dfs(1, 0)
    print(result)