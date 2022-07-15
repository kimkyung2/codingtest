# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 11:53:24 2022

@author: kki
"""

# 2504번 괄호의 값
# 올바른 괄호열이란?
# 1) 한 쌍의 괄호로만 이루어진 () 와 []는 올바른 괄호열
# 2) 만일 x 가 올바른 괄호열이면 (x)나 [x] 모두 올바른 괄효열
# 3) x와 y 모두 올바른 괄호열이라면 이들을 결합한 xy도 올바른 괄호열
# 우리는 어떤 올바른 괄호열 x에 대하여 그 괄호열의 값을 아래와 같이 정의하고 값(x)로 표시
# 1) ()인 괄호열의 값은 2
# 2) []인 괄호열의 값은 3
# 3) (x) 괄호값은 2x값(x)로 계산됨
# 4) [x] 괄호값은 3x값[x]로 계산됨
# 5) 올바른 괄호열 x와 y가 결합도니 xy의 괄호값은 값(xy) = 값(x) + 값(y)로 계산됨


n = list(input())

stack = []
result = 0
tmp = 1

for i in range(len(n)):
    if n[i] == '(': # 여는 괄호여서 단순히 stack에 push 함
        tmp *= 2
        stack.append(n[i])
    
    elif n[i] == '[':
        tmp *= 3
        stack.append(n[i])
        
    elif n[i] == ')': # 닫는 괄호 중 ')'일 떄, 스택의 top에 있는 것이 '[' 이거나 스택이 비었다면 에러
        if not stack or stack[-1] == '[':
            result = 0
            break
        
        if n[i-1] == '(':
            result += tmp
        stack.pop()
        tmp //= 2 # 괄호 입력 배열에서 그 괄호의 바로 직전의 괄호가 쌍이 맞는 경우에만 곱하기
        
        
    else: #  닫는 괄호 ']' 일 때, 스택의 top에 있는 것이 '(' 이거나 스택이 비었다며 에러
        if not stack or stack[-1] == '(':
            result = 0
            break
        if n[i-1] == '[':
            result += tmp
        stack.pop()
        tmp //= 3
        
if stack:
    result = 0
print(result)