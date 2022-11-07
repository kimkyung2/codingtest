# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:37:24 2022

@author: kki
"""

# 16953번 A -> B
# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
# 2를 곱한다.
# 1을 수의 가장 오른쪽에  추가한다.
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
# 만들 수 없는 경우는 -1 출력


a, b = map(int, input().split())

# 핵심은 a를 b로 만드는 게 아니라, b를 a로 만든다.

cnt = 1

while b != a:
    if a == b:
        break
    elif a > b:
        cnt =- 1
        break
    elif b%10 == 1:  # 처음에 10으로 나눈 나머지가 1인 것을 체크
        b//=10
        cnt += 1
    elif b%2 == 0: # 2로 나눈 나머지가 0인것들을 체크, B를 계속 수정하여 A에 도달하도록 함.
        b//=2
        cnt += 1
    else:
        cnt =- 1
        break
    
print(cnt)
