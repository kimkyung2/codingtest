# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 12:45:13 2022

@author: kki
"""

# 10569번 다면체
# 임의의 볼록다면체에 대해 (꼭짓점의 수) - (모서리의 수) + (면의 수) = 2가 성립할 때,
# 꼭짓점과 모서리의 수만 세고 면의 수는 세지 않을 때 면의 수를 구해라.


T = int(input())

for _ in range(T):
    
    v, e = map(int, input().split())
    
    m =  -v + e +2
    
    print(m)