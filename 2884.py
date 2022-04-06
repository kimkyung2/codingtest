# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:18:32 2022

@author: kki
"""

# 2884번 알람 시계
# 상근이가 일찍 일어나기 위해 창영이가 알려준 방법 '45분 일찍 알람 설정하기'
# 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것
# 현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이 방법을 사용한다면
# 언제로 고쳐야 하는지 프로그램 작성

# 첫째줄에 두 정수 H와 M 주어짐(현재 상근이가 설정한 알람 시간 H시 M분 의미)
# 입력시간은 24시간 표현을 사용함
# 24시간 표현에서 하루의 시작은 0:0(자정), 끝은 23:59(다음날 자정 1분 전)
# 시간을 나타낼 때, 불필요한 0은 사용하지 않음


H, M = map(int, input().split())

# 45분 일찍 알람을 설정하기 때문에, M의 값이 45보다 크면 -45를 하면 됨
# M이 45분 보다 작으면 H(시간)에서 -1을 하고, M에다가 +15를 더해줘야 함
# H가 0이면 H = 23으로 변경

if M >= 45:
    print(H, M-45)
elif M <= 44 and H >= 1:
    print(H-1, M+15)
else:
    print(23, M+15)
 
    
