# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 16:03:58 2022

@author: kki
"""

# 퀵 정렬 : 특정한 값을 기준으로 큰 숫자와 작은 숫자를 서로 교환한 뒤에 배열을 반으로 나눔

array = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(array)

def quick(array,start, end):
    if start >= end:
        return 
    pivot = start # 피벗은 첫번째 원소
    left = start +1
    right = end
    
    while left <= right: # 왼쪽 값이 오른쪽 값보다 커질 때 까지 반복
        while left <= end and array[left] <= array[pivot]: # 키 값보다 큰 값을 만날 때 까지 반복
            left += 1
        while right > start  and array[right] >= array[pivot]: # 키 값보다 작은 값을 만날 때 까지 반복
            right -= 1
        
        if left > right: # 엇갈린 상태면 키 값 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 left와 right 교체
            array[left], array[right] = array[right], array[left]
    
    quick(array, start, right-1)
    quick(array, right +1, end)
    
quick(array, 0, len(array)-1)
print(array)

