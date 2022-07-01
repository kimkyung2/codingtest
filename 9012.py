# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 12:02:05 2022

@author: kki
"""

# 9012번 괄호
# 한 쌍의 괄호 기호로된 () 문자열은 기본 VPS라 부름
# "(())()"와 "((()))"는 VPS 지만 "(()("와 "((()))())"는 VPS가 아닌 문자열
# 입력으로 주어진 괄호 문자열이 VPS인지 아닌지를 판단해서 결과를 YES와 NO로 나타내기

T = int(input())


for _ in range(T):
    v = input()
    ls = list(v)
    a = 0 
    
    for i in ls:
        if i == "(": # ls의 i가 ( 일 때 a 의 값을 1씩 증가
            a += 1
        elif i ==")": # ls의 i가 ) 일 때 a의 값은 -1씩 증가
            a -= 1
        if a < 0: # a의 값이 0보다 작으면 )의 개수가 더 많은 것으로 VPS가 아님
            print("NO")
            break
            
    if a == 0: # a의 값이 0이면 VPS 이므로 YES 출력
        print("YES")
    elif a > 0: # a의 값이 0보다 크면 (의 개수가 더 많은 것으로 VPS가 아님
        print("NO")
            