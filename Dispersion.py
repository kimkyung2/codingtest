# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:56:07 2022

@author: kki
"""

# 1009번 분산처리
# 마지막 데이터가 처리될 컴퓨터의 번호 찾기
# 조건 
# 1. 데이터의 개수는 항상 a^b의 형태로 주어짐
# 2. 컴퓨터는 10대
# 3. 처리 방법은 1번 데이터는 1번 컴퓨터, 2번 데이터는 2번 컴퓨터 ,,,,, 10번 데이터는 10번 컴퓨터, 11번 데이터는 1번 컴퓨터,,,

# 풀이 : 1부터 10까지 각각 거듭제곱했을 때 일의 자리의 패턴을 정리해서 구해야한다.
# 1) 패턴이 하나인 것: 1, 5, 6, 10
#  1, 5, 6은 자기 자신을 그대로 출력하게 하고, 10일때는 0이므로 10(컴퓨터 번호)출력
# 2) 패턴이 2개인 것 : 4, 9
#  b를 10으로 나눈 나머지를 구하고, 나머지가 0이면 그대로 a 출력, 아니면 a*a 일의 자리 출력
# 3) 패턴이 4개인 것 : 2, 3, 7, 8
#  b를 10으로 나눈 나머지가 0이면 a 출력, 아니면 a를 b의 나머지 만큼 거듭제곱한 것의 나머지 출력 

T = int(input())
a= []
b= []

for _ in range(T):
    num1, num2 = map(int, input().split())
    a.append(num1)
    b.append(num2)
    
for i in range(T):
    com = a[i]%10
    
    if com == 0:
        print(10)
    elif com in [1, 5, 6]:
        print(com)
    elif com in [4, 9]:
        if b[i]%2 == 0:
            print(com**2%10)
        else:
            print(com)
    else:
        if b[i] % 4 ==0:
            print(com**4%10)
        else:
            print(com**(b[i]%4)%10)