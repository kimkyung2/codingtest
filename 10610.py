# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 12:20:34 2023

@author: kki
"""

# 10610번 30
# 30의 배수가 되는 가장 큰 수를 만들어라

# 30의 배수가 되는 조건 : 일의 자리수가 0이여야 함, 각 자리의 숫자들을 더했을 때 3으로 나누어 떨어져야 함.

n = list(input())
n.sort(reverse = True)
sum = 0

if '0' not in n: # input의 디폴트인 string으로 받았기에 0을 문자로 적음
    print(-1)

else:
    for i in n:
        sum += int(i)
    if sum % 3 != 0: # 3의 배수 체크
        print(-1)
    else:
        print(''.join(n))