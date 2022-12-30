# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 13:57:19 2022

@author: kki
"""

# 1316번 그룹 단어 체커
# 그룹 단어란 단어에 존재한느 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면, ccazzzzbb는 c,a,z,b가 모두 연속해서 나타나고, kin도 k,i,n이 연속해서 나타나기 때문에 그룹단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 문자열의 첫 원소부터, 뒤의 나머지 원소와 비교하면서, 같은 게 있는지 확인
# 다음 원소와 같지 안혹, 그 이후 원소와 같으면 그룹단어 탈락

n = int(input())

group_word = 0

for _ in range(n):
    word = input()
    error = 0
    for index in range(0, len(word)-1): # index 범위 생성 : 0부터 단어 개수 -1까지
        if word[index] != word[index+1]: # 연달아 있는 두 문자가 다를 때,
            new_word = word[index + 1:] # 현재 글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0: # 남은 문자열에서 현재 글자가 있었다면
                error += 1 # error에 1씩 증가
                
    if error == 0:
        group_word += 1 # error가 0이면 그룹단어
print(group_word)



