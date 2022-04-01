# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:13:56 2022

@author: kki
"""

# 1011번 Ply me to the alpha centauri
# 우주선이 이전 작동시기에 k광년을 이동하였을 때는 k-1광년 혹은 k+1광년만을 다시 이동할 수 있음
# 예) 처음 작동시킬 경우 -1, 0, 1 광년을 이론상으로 이동할 수 있지만 사실상 음수와 0은 이동이유가 없으므로 1광년 이동할 수 있으며,
# 다음에는 0, 1, 2광년을 이동할 수 있는 것이다.
# 김우현은 이 점을 알고있기 떄문에 x와 y을 향해 최소한의 작동 횟수로 이동하ㅕㄹ 함
# y지점에 도착해서도 공간 이동 장치의 안전성을 위하여 y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 함
# x지점과 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램 작성

# x,y는 정수로 주어지며, x는 항상 y보다 작은 값을 갖음

T = int(input())

for _ in range(T):    
    x, y = map(int, input().split())
    distance = y - x # 우현이가 이동해야할 거리
    cnt = 0 # 이동 횟수
    move = 1 # cnt별 빈도수
    move_plus = 0 # 이동한 거리의 합
    
    while move_plus < distance:
        cnt += 1 
        move_plus += move  # count 수에 해당하는 move를 더함
        if cnt %2 == 0: # cnt가 2의 배수일 때, 
            move +=1
    print(cnt)
    
#  cnt가 증가할때마다 해당 cnt에 따라 이동할 수 있는 거리르 합해가면서 처음에 받은 이동거리에 도달하면 반복문을 멈춰서 cnt를 구하는 방식
