# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:03:48 2022

@author: kki
"""

# 1967번 트리의 지름
# 트리는 사이클이 없는 무방향 그래프이다. 트리에는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다.
# 트리에서 어떤 두노드를 선택해서 양쪽으로 쫙 당길때, 가장 길게 늘어나는 경우가 있다. 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝점으로 하는 원안에 들어간다.
# 이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.
# 입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오.
# 트리의 노드는 1부터 n까지 번호가 매겨져 있다.

# 트리의 지름은 bfs 두번을 사용하여 간단하게 o(n)의 시간복잡도로 구현이 가능
# 1) 트리에서 아무 노드나 잡고 그 노드에 대한 가장 먼 노드를 구하고 이 노드를 n1이라고 하자.
# 2) n1에 대한 가장 먼 노드를 한번 더 구한다. 이 노드를 n2라고 하자.
# 3) 이제 n1과 n2의 거리가 트리의 지름이 된다.

# def dfs(x, y): # dfs 탐색, 시작 노드 번호, 현재 노드 가중치
#     for  a, b in graph[x]: # 반복문을 통해 현재 노드와 연결된 노드, 연결된 노드의 가중치를 확인한다.
#         if visited[a] == -1: # 탐색하지 않은 노드라면 탐색한다.
#             visited[a] = y + b # 이전 노드의 가중치와 현재 노드의 가중치를 더한다.
#             dfs(a, y+b) # 재귀적으로 연결된 모든 노드를 탐색
            
# n = int(input())

# # 각 노드가 연결된 정보를 트리로 표현
# graph = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     a, b, c = map(int, input().split())
#     graph[a].append([b, c])
#     graph[b].append([a, c])

# visited = [-1] * (n+1) # 탐색 확인, 가중치 확인
# visited[1] = 0 # 시작 노드는 가중치를 0으로 초기화
# dfs(1, 0) # 첫 번째 노드를 dfs 탐색

# # 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
# start = visited.index(max(visited))

# visited = [-1] * (n+1) # 탐색확인, 가중치 확인
# visited[start] = 0 # 가장 먼 노드의 가중치를 0으로 초기화
# dfs(start, 0) # 가장 먼 노드를 dfs 확인

# print(max(visited))


# 시작점에서 가장 먼 노드를 찾고, 이 노드로부터 가장 먼 노드를 찾으면 그 결괏값이 가장 먼 노드이다.
# 따라 bfs 두번으로 해결할 수 있다. v와 e의 맥스값이 10000이므로 bfs의 시간복잡도인 o(v+e)내에 해결할 수 있다.
from collections import deque

def bfs(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque()
    queue.append(start)
    
    while queue:
        curr = queue.popleft()
        for i, cost in tree[curr]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[curr] + cost
    m = max(visited)
    return [visited.index(m), m]

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    start, end, weight = map(int, input().split())
    tree[start].append([end, weight])
    tree[end].append([start, weight])

print(bfs(bfs(1)[0])[1])