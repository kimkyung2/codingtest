# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 02:28:14 2022

@author: quffh
"""

# 공유기 설치
# c개의 공유기를 N개의 집에 설치해서 가장 인접한 두 공유기 사이의 거리 최대값 구하기
# 조건
# 1. 집의개수와 공유기의 개수가 하나 이상의 빈 칸을 사이에 두고 주어짐
# 2. N개줄에서 집의 좌표를 나타내는 xi가 한줄에 하나씩 주어짐
# 풀이 : 이진탐색을 사용하여 푼다

n,c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))
    
array.sort()

def binary(array, start, end): # 시작값은 최소거리, 끝값은 최대거리
    while start <= end:
        mid = (start + end) //2
        current = array[0]
        count = 1
     
    for i in range(1, len(array)):
         if array[i] >= current + mid:
             count += 1
             current = array[i]
             
    if count >= c: # 설치한 공유기 개수가 c를 넘어가면 더 넓게 설치해야 하므로 설치거리를 mid+1로 설정하여 다시 설치
        global answer
        start = mid + 1
        answer = mid
    else: # c를 넘어가면 더 좁게 설치해야 하므로 mid-1설정
        end = mid -1

start = 1
end = array[-1] - array[0]
answer = 0

binary(array, start, end)
print(answer)
