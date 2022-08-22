# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 11:43:43 2022

@author: kki
"""

# 11758번 CCW
# 2차원 좌표 평면 위에 있는 점 3개 p1,p2,p3가 주어진다.
# p1,p2,p3를 순서대로 이은 선분이 어떤 방향을 이루고 있는지 구하는 프로그램을 작성

arr = []
for i in range(3):
    arr.append(list(map(int,input().split()))) 

# 위랑 같은 코드 : arr = [list(map(int, input().split())) for _ in range(3)]

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    return (x1*y2 + x2*y3 + x3*y1)- (x2*y1 + x3*y2 + x1*y3)

result = ccw(arr[0], arr[1], arr[2])

# vec1과 vec2는 벡터 a,b에 해당하고 result 값은 외적 값에 해당
# vec1 = [arr[1][0] - arr[0][0], arr[1][1] - arr[0][1]] 
# vec2 = [arr[2][0] - arr[1][0], arr[2][1] - arr[1][1]]
# result = (vec1[0]*vec2[1] - vec1[1]*vec2[0])

if result < 0:
    print(-1)
elif result > 0:
    print(1)
else:
    print(0)