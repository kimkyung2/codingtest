# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:31:36 2022

@author: kki
"""

# 2468번 안전영역
# 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇개가 만들어 지는 지를 조사
# 문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정함

# 물에 잠기지 않는 안전한 영역은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽, 왼쪽으로 인접해 있으며 그 크기가 최대인 영역을 말함
# 꼭짓점만 붙어있는 두 지점은 인접하지 않는다고 취급

# 어떤 지역의 높이 정보가 주어졌을 때, 장마철 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성

# 비는 얼마나 오는지 모름 -> 비가 오는 양은 0부터 배열에 있는 최고 높이까지 옴
# 첫번째 줄은 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 N 입력
# 두번째 줄은 N개의 각 줄에는 2차원 배열의 첫번째 행부터 N부터 행까지 순서대로 한 행씩 높이 정보가 입력됨.

# 풀이
# 1. BFS 순회 '수위'와 '건물 높이'를 각 수행마다 비교하며 '구역'의 넓이를 구해야 함
# 수위 : 가장 낮은 건물의 높이보다 1 낮을 때 ~ 가장 높은 건물의 높이와 같을 때까지 모든 경우의 수를 완전 탐색

from collections import deque

# 상하좌우 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 선언
n = int(input()) # 지도 한변의 길이
map_list = [] # 지도 받을 빈 리스트
max_heights = 0 # 가장 높은 건물의 높이
mx_area = 0 # 구역의 갯수 최대값

for i in range(n):
    inp = list(map(int, input().split()))
    map_list.append(inp) # 입력받은 높이를 지도에 저장 ## map_list.append(list(map(int, input(). split())))도 가능
    
    for j in range(n):
        if map_list[i][j] > max_heights:
            max_heights = map_list[i][j] # 그래프의 원소 중 최대값을 찾음

# 연산
def bfs(x, y, water_level):
    # bfs 시작점
    q = deque() # 큐 선언
    q.append((x, y)) # 시작점을 큐에 삽입
    visited[x][y] = 1

    while q: # 큐가 비어있지 않을 때
        x, y = q.popleft() # 좌표 확인
        
        for i in range(4): # 각각 이동한 후의 새로운 좌표값
            nx = x + dx[i]
            ny = y + dy[i] # 상 하 좌 우
            
            if 0 <= nx < n and 0 <= ny <n:
                if visited[nx][ny] == 0 and map_list[nx][ny] > water_level:
                    visited[nx][ny] = 1 # 방문 표시
                    q.append((nx, ny)) # q에 더해준 후

for water_level in range(max_heights): # 해당 경우의 수를 분석, 비가 안오는 경우인 0부터 max-1까지 조회(max는 모든 지역이 물에 잠기므로 안전영역이 0이므로 고려할 필요 없음)
    area = 0 # 현재 구역의 수
    visited = [[0]*n for _ in range(n)] # 방문 리스트 선언, 매 높이마다 조회를 해야하므로 visited를 매번 정의
    
    for i in range(n):
        for j in range(n):
            if map_list[i][j] > water_level and visited[i][j] == 0: # 방문하지 않았고 수위보다 높은 지점, 비가 온 것보다 높은 곳이고 방문하지 않은 경우 bfs 호출
                visited[i][j] = 1 # 방문 표시 후
                bfs(i, j, water_level) # BFS 연산
                area += 1 # BFS가 한 번 시행될때마다 구역의 개수 1개 가산
    
    if area > mx_area: 
        mx_area = area # 구역의 개수 최대값을 갱신
print(mx_area)



















