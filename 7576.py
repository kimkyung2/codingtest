# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 11:32:25 2022

@author: kki
"""

# 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익음
# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향을 의미
# 대각선 토마토에는 영향을 주지 못함, 토마토가 혼자 저절로 익는 경우는 없다고 가정
# 창고에 보관된 토마토들이 며칠이 지나면 다 익는지에 대한 최소 일수 알아내기
# 상자의 일부 칸에는 토마토가 들어 있지 않을 수도 있음

# M은 상자의 가로 칸 수 , N은 상자의 세로 칸 수
# 토마토의 정보를 입력할 떄
# 정수 1은 익은 토마토, 정수 0은 익지않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

# 토마토가 모두 익을 떄까지의 최소 날짜를 출력
# 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력하고 토마토가 모두 익지 못하는 상황이면 -1을 출력

# bfs 사용하기 
from collections import deque
m, n = map(int, input().split())

matrix = []

for _ in range(n): # 이중 배열
    matrix.append(list(map(int, input().split())))
    
dx = [1, -1, 0, 0] # 동서남북 배열 선언
dy = [0, 0, -1, 1]

res = 0

queue = deque()
for i in range(n): # 큐에 처음 받은 토마토의 위치 좌표를 append
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append((i,j))

while queue:
    x, y, = queue.popleft() # 처음 토마토 좌표 x,y에 꺼내고
    for i in range(4): # 토마토 사분면의 익힐 토마토들을 찾아봄
        _x = dx[i] + x
        _y = dy[i] + y
        if 0<= _x < n and 0 <= _y < m and matrix[_x][_y] == 0: # 해당 좌표가 좌표 크기보다 넘으면 안되고 그 좌표 토마토가 0일 떄
            matrix[_x][_y] = matrix[x][y] + 1 # 토마토를 익히고 1을 더해주면서 횟수 세기
            queue.append((_x,_y))             # 여기서 나온 제일 큰 값이 정답이 됨
            
for i in matrix:
    for j in i: 
        if j ==0:
            print(-1) # 다 찾아보았는데 토마토를 익히지 못했으면 -1 출력
            exit(0)
    res = max(res, max(i)) # 다 익혔다면 최댓값이 정답
# 처음 시작을 1로 표현해서 1을 빼줌    
print(res -1)
            