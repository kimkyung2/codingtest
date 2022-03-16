# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:35:58 2022

@author: kki
"""

# 1918번 후위 표기식
# 후위 표기법은 연산자가 피연산자 뒤에 위치함
# 후위 표기법의 예) a+b*c 일 때 abc*+이 됨
# 중위 표기식이 주어졌을 때 후위 표기식으로 고치는 프로그램 작성
# 수식의 피연산자는 알파벳 대문자로 이루어지며 수식에서 한 번씩만 등장
# -A+B 같이 -가 가장 앞에 오거나 AB와 같이 *가 생략되는 등의 수식은 주어지지않음
# 표기식은 알파벳 대문자와 +, -, *, /, (, ) 로만 이루어짐

# 연산자 우선 순위
# 1. (,)
# 2. *,/
# 3. +,-

# 스택, 큐 사용해서 풀기

text = input()
stack = []
ans = ''

for i in text:
    if i.isalpha(): # 연산자가 아니면 ans에 더하기(ans -> 최종식)
        ans += i
    else:
        if i == '(' : # ( 연산자면 stack에 삽입 : stack == 연산자 저장 스택
            stack.append(i)
        elif i =='*' or i == '/': # '*', '-'은 stack에 추가하기전에 stack에 존재하는 '*', '/'를 pop하여 결과값에 저장
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-': # '+', '-'는 stack에 추가하기 전에 stack에 존재하는 '(' 직전까지의 값들을 모드 pop 하여 결과값에 저장
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(i)
        elif i == ')': # ')'는 stack에 존재하는 '(' 직전까지의 값들을 모두 pop 하여 결과값에 존재하고, stack에서 '(' 제거를 위해 pop을 추가로 한 번 더 수행
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        

while stack:
    ans += stack.pop()
    
print(ans)