# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:28:11 2022

@author: kki
"""

# 2108번 통계학
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다.
# 단, N은 홀수라고 가정
# 1. 산술평균: N개의 수들의 합을 N으로 나눈 값
# 2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성
from collections import Counter

n = int(input())

li = []
for i in range(n):
    li.append(int(input()))


# 산술평균
print(round(sum(li)/n)) 

# 중앙값
li.sort()
print(li[n//2])

# 최빈값(1)
# cnt = Counter(li).most_common() 
# # 최빈값이 여러개일 때, 두번째로 작은 값을 출력하기 위해서 most_common(2)를 활용, 빈도수가 높은 숫자 2개를 가져옴
# # 만약 li의 길이가 2이상이면 2번째로 작은 값 출력, 그렇지 않은 경우 가장 빈도수가 높은 값을 그대로 출력
# print(cnt)
# if len(li) > 1:
#     if cnt[0][1] == cnt [1][1]:
#         print(cnt[1][0])
#     else:
#         print(cnt[0][0])
# else:
#     print(cnt[0][0])

# 최빈값(2)
mode_li = [li[0]] # 최빈값 리스트 초기화값 생성( li에 있는 첫번째 숫자 입력)
cnt = 1 # 현재 숫자 개수를 세는 변수
cnt_max = 0 # 최빈값에 해당하는 개수 변수
last = li[0] # 이전 숫자에 해당하는 변수

for i in li[1:]: # 숫자 하나씩 받으면서
    if i != last: # 이전 숫자와 현재 숫자가 불일치하고
        if cnt > cnt_max: # 특정 수의 개수가 현재 최빈값 개수보다 많다면
            mode_li = [] # 최빈값 리스트 초기화
            mode_li.append(last) # 최빈값 리스트에 새로운 최빈값 추가
            cnt_max = cnt
        elif cnt == cnt_max and last not in mode_li: # 특정 수의 개수가 현재 최빈값 개수와 같다면 최빈값 추가
            mode_li.append(last) 
        cnt = 1
    else: # 중복된 수가 존재한다면 cnt 개수 추가
        cnt += 1
    last = i

# 마지막 수 계산
if cnt > cnt_max:
    mode_li = [last]
elif cnt == cnt_max and last not in mode_li:
    mode_li.append(last)
    
# 최빈값이 1개라면 단일값 출력    
if len(mode_li) == 1:
    print(mode_li[0])
else: # 최빈값이 여러개라면 두번째로 작은 값 출력
    print(mode_li[1])

# 범위
print(max(li) - min(li))   