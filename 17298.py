# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 13:25:37 2023

@author: kki
"""

# 17298번 오큰수
# 크기가 n인 수열 a = a1, a2, .... , an이 있다. 수열의 각 원소 ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
# ai의 오큰수는 오른쪽에 있으면서 ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
# 그러한 수가 없는 경우에 오큰수는 -1 이다.

n = int(input())
arr = list(map(int, input().split()))
stack = []
NGE = [-1]*n # 기본적으로 오큰수가 없으면 -1을 출력해야 하므로 배열 NGE를 -1로 초기화해줌

for i in range(n): # 입력받은 수들 배열 arr을 탐색
    while stack and arr[stack[-1]] < arr[i]: # stack이 비어있지 않고, arr[스택 맨 위]가 arr[i]보다 작으면 반복
        NGE[stack.pop()] = arr[i] # NGE의 stack.pop()한 인덱스 자리에 arr[i]를 넣음
    stack.append(i) # stack에 i를 넣음.
print(*NGE) # print할 때, 앞에 *을 붙이면 공백을 기준으로 원소들만 나열됨.