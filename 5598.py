# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 19:15:32 2022

@author: kki
"""

# 5598번 카이사르 암호
# 카이사르는 편지를 쓸 때, 알파벳 문자를 3개씩 건너뛰어 적었다고 한다.
# 26개의 대문자 알파벳으로 이루어진 단어를 카이사르 암호 형식으로 4문자를 옮겨 겹치지 않게 나열하여 얻은 카이사르 단어가 있을 때, 
# 이 카이사르 단어를 원래 단어로 돌려놓는 프로그램 작성

n = input()
result = ''

for i in n:
    if  68 <= ord(i) <= 90:
        result += chr(ord(i)-3)
    else:
        result += chr(ord(i)+23)
        
        
print(result)
        
        
        