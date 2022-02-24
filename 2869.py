# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 16:37:05 2022

@author: kki
"""

# 2869번 달팽이는 올라가고 싶다
# 달팽이가 높이 V미터인 나무 막대를 올라간다
# 낮에는 A미터 올라갈 수 있지만, 밤에 자는 동안 B미터 미끄러진다.
# 정상에 올라간 후에는 미끄러지지 않는다
# 달팽이는 며칠만에 정상에 올라갈 수 있는가
# 조건 : 첫째줄에 세정수가 공백으로 구분되어서 주어짐

import math

A, B, V = map(int, input().split())

sun = (V-B)/(A-B) # 정상에 한번 도달하면 밤에 미끄러지지 않는 것을 고려해
print(math.ceil(sun))
