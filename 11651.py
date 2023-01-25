# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:53:01 2023

@author: kki
"""

# 11651번 좌표 정렬하기2
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성

n = int(input())
array = [] # array 변수 만들어서 리스트 미리 초기화

for i in range(n): # n변수에 테스트 케이스의 수를 입력받은 후 그만큼 for문으로 반복
    x, y = map(int, input().split())
    array.append([y,x]) # 예제 출력 값이 y를 기준으로 정렬되게끔 y,x 순으로 append
    
s_array = sorted(array)

for y, x in s_array:
    print(x, y)
    