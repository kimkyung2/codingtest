# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:55:45 2022

@author: kki
"""

# 1012번 유기농 배추
# 최소 배추흰지렁이의 마리 구하기
# 배추가 인접(상하좌우)해 있으면 그 부분도 배추흰지렁이가 해충을 보호해줌
# 배추가 몇 군데에 퍼져있는지 조사
# 두 배추의 위치가 같은 경우 없음
# 0은 배추가 심어져 있지 않은 땅, 1은 배추가 심어져 있는 땅
# T = 테스트 케이스, M = 배추밭의 가로길이, N = 배추밭의 세로길이, K = 배추가 심어져 있는 개수
# 풀이 : BFS를 사용

from collections import deque

T = int(input())

for i in range(T): # T 횟수만큼 반복
    M, N, K = map(int, input().split())
    graph = [] # 밭과 유기농 배추의 상태
    queue = deque()
    
    for j in range(M): #밭의 크기에 맞게 0으로 정의함
        graph.append([0]*N)
    
    for _ in range(K): # K개만큼의 배추의 위치를 입력받고 이것을 밭 상태에 적용, 어느 위치에 배추가 심어져 있는지 입력함
        x, y = map(int, input().split())
        graph[x][y] = 1
    cnt = 0 # cnt는 최종 구역 개수를 셈, 이때 여러 케이스 반복되므로 0으로 초기화해야함
    
    for i in range(M): # 연결된 배추를 엮어서 파악해야하지만 기본적으로 모든 좌표를 탐색
        for j in range(N): # deque 자료 구조 안에 ㅎ나번씩 모든 좌표를 탐색하도록 함
            queue.append((i,j))
            x,y = queue.popleft()
            if graph[x][y] == 1: # 배추가 감지되는 좌표만 탐색되도록 걸러줌, 배추가 없는 좌표는 고려할 필요가 없음
                queue.append((x,y))
                cnt += 1
                
            while queue: # while을 사용하면 deque 자료 구조 안에 모든 자료를 꺼낼 때까지 while문을 돌려 탐색
                x,y = queue.popleft() # queue.popleft()로 가장 먼저 들어온 좌표를 꺼내 x,y에 매핑하도록함
                if x < 0 or y < 0 or x >= M or y >= N: # 이때 탐색하고자 하는 위치인 x,y가 valid한 지 확인해야 하므로 밭 위치내에 있는지 확인함
                    continue
                if graph[x][y] == 1: # 밭에서 배추가 1로 있다고 판단하는 경우, 0으로 변경 해줌과 동시에 밭의 상하좌우 위치를 확인해야함.
                    graph[x][y] = 0  # 따라서 deque 자료 구조에 상하좌우 위치를 넣음, 이렇게 되면 while문이 돌면서 해당 위치들을 검토하고 필요하면 0으로 변경함
                    queue.append((x, y+1)) # 이 때 중요한 점은 해당 값은 cnt를 올리지 않는다는 것, while문 내에서만 처리되고 cnt 값은 올라가지 않음
                    queue.append((x, y-1))
                    queue.append((x+1, y))
                    queue.append((x-1, y))                    
    print(cnt)    


