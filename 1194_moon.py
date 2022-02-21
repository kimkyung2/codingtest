# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 17:56:01 2022

@author: kki
"""

# 1194번 달이 차오른다, 가자
# 민식이가 달 여행길을 가기 위해 미로를 탈출해야 함
# 미로는 직사각형, 한번의 움직임은 현재 위치에서 수평이나 수직으로 한 칸 이동하는 것
# 미로 탈출하는데 걸리는 이동 횟수의 최솟값을 구하기

# 조건
# 1. 빈 칸: 언제나 이동할 수 있음('.')
# 2. 벽: 절대 이동할 수 음('#')
# 3. 열쇠: 언제나 이동할 수 있음. 이 곳에 처음들어가면 열쇠를 집음('a', 'b,' 'c', 'd', 'e', 'f')
# 4. 문: 대응하는 열쇠가 있을 때만 이동할 수 있음('A', 'B', 'C', 'D', 'E', 'F')
# 5. 민식이의 현재 위치: 빈곳이고, 민식이가 현재 서 있는 곳임('0')
# 6. 출구: 달이 차오르기 때문에, 민식이가 가야하는 곳, 이 곳에 오면 미로를 탈출('1')
# 문에 대응하는 열쇠 없을 수도 있음
# 0은 한 개, 1은 적어도 한 개 있음
# 열쇠는 여러번 사용할 수 있음

from collections import deque

n, m = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[[0]*64 for _ in range(m)] for _ in range(n)]
dx = -1, 0, 1, 0
dy = 0, 1, 0, -1
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            graph[i][j] ="."
            q.append((i, j, 0))
            break
        
while q:
    x, y, key = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nkey = key
        
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] !="#" and visited[nx][ny][key] == 0:
            # 문인 경우, 열쇠가 없으면 continue, &연산으로 1혹은 0이 나오게 됨
            if graph[nx][ny].isupper(): # 대소문자 확인 함수, 모든 문자열이 대문자면 Treu, 아니면 False를 리턴
                if not(key & 1<<(ord(graph[nx][ny]) - ord("A"))):
                    continue
        
            elif graph[nx][ny].islower():
                # 열쇠인 경우, or 연산을 통해 key를 교체, a키만 가지고 c키를 먹는다면 1->101이 됨
                nkey |= 1<<ord(graph[nx][ny]) - ord("a")
            elif graph[nx][ny] =="1":
                print(visited[x][y][key] + 1)
                exit()
            q.append((nx, ny, nkey))
            visited[nx][ny][nkey] = visited[x][y][key]+1
        
print(-1)
