# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 14:13:32 2022

@author: kki
"""
# 1758번 알바생 강호
# 강호가 8시에 입구에 서있는 손님들에게 커피를 줌
# 손님들은 강호에게 팁을 줌
# 팁 : 원래 주려고 생각했던 돈 - (들어가는 등수 -1) 원
# 위의 식이 음수라면 강호는 팁을 받을 수 없음
# 카페 앞에 있는 사람의 수 n, 각 사람이 주려고 생각하는 팁이 주어질 때, 강호가 받을 수 있는 팁의 최댓값

# 팁을 많이 받기 위해서는 손님이 팁 주려는 값이 많아야 한다.
# 손님이 줄 팁이 큰 순서대로 배열되어야함

n = int(input()) # 손님의 수
tip = [] # 팁의 배열

for _ in range(n):
    a = int(input())
    tip.append(a)
tip.sort(reverse = True)

rate = 1 # 등수 초기화
result = 0 # 결과값 초기화

for i in tip:
    if i - (rate -1) >= 0: # (주려고 한 팁) - (받은 등수 -1) 이 음수가 아닌 경우만 알고리즘 생성
        result = result + (i - (rate - 1))
        rate += 1
    else:
        continue
    
print(result)