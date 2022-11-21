# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:35:43 2022

@author: kki
"""

# 17387번 선분 교차2

# 2차원 좌표 평면 위의 두 선분 L1, L2가 주어졌을 때, 두 선분이 교차하는지 아닌지 구해보자.
# 한 선분의 끝 점이 다른 선분이나 끝 점 위에 있는 것도 교차이다.
# L1의 양 끝 점은 (x1, y1), (x2, y2) L2의 양 끝 점은 (x3, y3,),(x4, y4)
# 교차하면 1, 아닌 0 출력

point = []

x1, y1, x2 ,y2 = map(int ,input().split())
x3, y3, x4, y4 = map(int, input().split())

point.append([x1, y1])
point.append([x2, y2])
point.append([x3, y3])
point.append([x4, y4])

def ccw(p1, p2, p3):
    tmp = (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])
    if tmp > 0:
        return 1
    elif tmp <0:
        return -1
    else:
        return 0

def solution(p1, p2, p3, p4):
    is_result = False
    result = 0
    p123 = ccw(p1, p2, p3)
    p124 = ccw(p1, p2, p4)
    p341 = ccw(p3, p4, p1)
    p342 = ccw(p3, p4, p2)

    if p123 * p124  == 0 and p341 * p342 == 0:
        is_result = True
        if min(p1[0], p2[0]) <= max(p3[0], p4[0]) and min(p3[0], p4[0]) <=max(p1[0], p2[0]) and min(p1[1], p2[1]) <= max(p3[1], p4[1]) and min(p3[1], p4[1]) <= max(p1[1], p2[1]):
            result = 1
    else:
        if p123 * p124 <= 0 and p341 * p342 <= 0:
            if not is_result:
                result = 1
    return result

print(solution(point[0], point[1], point[2], point[3]))

# 1) ccw(A, B, C) * ccw(A, B, D) <= 0 && ccw(C, D, A)*ccw(C, D, B) <= 0
#   case 세 점이 한 직선에 있는 경우
# ccw(A, B, C) * ccw(A, B, D) == 0 && ccw(C, D, A) * ccw(C, D, B) == 0 : 점 2개가 겹침
# ccw(A, B, C) * ccw(A, B, D) < 0 && ccw(C, D, A) * ccw(C, D, B) == 0 : 하나의 선과 다른 선의 점이 겹침
# ccw(A, B, C) * ccw(A, B, D) > 0 && ccw(C, D, A) * ccw(C, D, B) == 0 : 하나의 선이 연장되면 가능한 경우

# 2) ccw(A, B, C) * ccw(A, B, D) = 0 && ccw(C, D, A)*ccw(C, D, B) = 0
#   case 네 직선이 한 직선상에 (일직선 상에 존재할 때)
# 교차하는 경우 : 점 B보다 점 C가 작고, 점 A보다 점 D가 커야함 A______D______B_______D
# 교차 안함 : A______B ------ C________D
