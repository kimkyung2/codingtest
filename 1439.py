# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:08:29 2022

@author: kki
"""

# 1439번 뒤집기
# 다솜이는 0과 1로 이루어진 문자열 S를 가지고 있다.
# 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다.
# 다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
# 뒤집는 것은 1을 0으로 0은 1로 바꾸는 것을 의미한다
# 문자열 S가 주어졌을때, 다솜이가 해야하는 행동의 최소 횟수를 출력하시오

s = input()

count0 = 0 # 전부 0으로 바뀌는 경우
count1 = 0 # 전부 1로 바뀌는 경우

# 첫번째 원소에 대해서 처리
if s[0] == '1':
    count0 += 1
else :
    count1 += 1
    
# 두번째 원소부터 모든 워소를 확인하며
for i in range(len(s) -1):
    if s[i] != s[i+1]:
        # 다음 수에서 1로 바뀌는 경우
        if s[i+1] =='1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 +=1
            
print(min(count0, count1))