# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 16:43:59 2022

@author: kki
"""
# 병합정렬 : 하나의 문제를 두 개의 작은 문제로 분할한 뒤에 각자 계산하고 나중에 합치는 방법을 사용

array = [7, 6, 5, 8, 3, 5, 9, 1]
print(array)

def merge(array):
    n = len(array)  
    
    if n <= 1 : # n이 1개 이하면 종료
        return
    # 배열을 두 그룹으로 절반씩 나눔
    mid = n//2
    array_front = array[:mid]
    array_back = array[mid:]
    merge(array_front)
    merge(array_back)
    
    i = 0 # 배열 앞 부분 재귀호출 함수 제한하기
    j = 0 # 배열 뒤 부분 재귀호출 함수 제한하기
    k = 0 # 옮길 자리의 숫자
    
    # 결합
    while i < len(array_front) and j < len(array_back):
        if array_front[i] < array_back[j]: # 여기 부등호 바꾸면 내림차순
            array[k] = array_front[i]
            i += 1
            k += 1
        else:
            array[k] = array_back[j]
            j += 1
            k += 1
            
    # 결합하고 남은 것 추가
    while i < len(array_front):
        array[k] = array_front[i]
        i += 1
        k +=1
    while j < len(array_back):
        array[k] = array_back[j]
        j += 1
        k += 1
        
merge(array)
print(array)