# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 20:48:02 2022

@author: kki
"""

# 11050번 이항계수1
# 자연수 N과 정수 K가 주어졌을 때 이항 계수 (N/K)를 구하는 프로그램을 작성하시오

# 이항계수는 경우의 수를 계산할 떄 사용하는 것, n개의 서로 다른 것들 중에서 k개를 선택하는 것의
# 조합의 경우의 수를 구한느 것
# (n)(k)는 nCk 조합으로 나타낼 수 있다.(=  n!/k!(n-k!) )


# 재귀를 사용해서 풀이

n, k = map(int, input().split())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(n) // (factorial(n-k) * factorial(k)))

# 반복문을 사용해서 풀이( nCk = n*(n-1)(n-2)..../k!)

n, k = map(int, input().split())

result = 1
for i in range(k):
    result *= n
    n -= 1
    
divisor = 1
for i in range(2, k+1):
    divisor *= i

print(result // divisor)