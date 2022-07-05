# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 10:53:46 2022

@author: kki
"""

# 1783번 병든 나이트
# 병든 나이트가 N x M 크기 체스판의 가장 왼쪽아래 칸에 위치해 있다.
# 건강한 나이트와 다르게 4가지로만 움직일 수 있다.
# 1) 2칸 위로, 1칸 오른쪽
# 2) 1칸 위로, 2칸 오른쪽
# 3) 1칸 아래로, 2칸 오른쪽
# 4) 2칸 아래로, 1칸 오른쪽
# 방문한 칸의 수를 최대로 할 때, 이동 횟수가 4번보다 많다면, 이동 방법을 모두 한번씩 사용해야한다.
# 이동 횟수가 4번보다 적은 경우에는 이동 방법에 대한 제약이 없다.

n, m = map(int, input().split())

if n == 1: # n = 1 일 때, 현재 칸 외에는 이동 가능한 칸이 없음
    print(1)
elif n == 2: # 위아래로 한칸씩 움직일 수 있음, 따라서 가로로 2칸씩 몇 번 이동할 수 있는지 계산해야함,
    print(min(4, (m-1)//2 +1)) # (m-1)//2에 +1을 한 이유 : 이동 가능 횟수는 총 3번이다 4번이상이 되면 이동법 전부 사용해야되기 때문
                               # m-1은 가로길이 m 중에서 현재 위치를 빼야 하기 때문이고 //2는 2칸씩 이동하므로 그 값을 제외해주기 위함
                               # 여행 중 동일한 칸을 중복할 수 없기 때문에 첫번째 칸을 빼줘야한다.
elif m < 7 and n >=3: # n=3일 때, 최대로 이동하기 위해서는 위아래 2칸씩 이동하고 오른쪽으로는 1칸씩 이동해야한다.
                      # 이동 가능 횟수는 3번이하로 3이나 m-1 중 작은값과 같으며, 방문한 칸수는 4, m중 작은 값과 같다.
    print(min(4, m))
else:
    print((2+(m-5))+1) # m>=7일 때, 4번의 경우를 수를 다 이용해야하고, 최대로 가기위해서는 1,4번 이동을 반복하는 것이 좋다.
                       # 2(2번과 3번이 이동한 횟수)이고, m-5는 m개의 길이 중  2,3번 이동한 4칸,  첫번째 칸을 뺀 값이다.
                       # 최대 방문 가능한 칸 수는 이동횟수 + 1이다
      
    