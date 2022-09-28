# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 16:02:02 2022

@author: kki
"""

# 10825번 국영수
# 학생 성적을 정렬하는 프로그램을 작성
# 1) 국어 점수가 감소하는 순서로
# 2) 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 3) 국어점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4) 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 옴)

t = int(input())
li = []

for i in range(t):
    score = input().split()
    
    li.append([score[0], int(score[1]), int(score[2]), int(score[3])])
    
li_sort = sorted(li, key = lambda x : (-x[1], x[2], -x[3], x[0]))
                     
for j in li_sort:
    print(j[0])