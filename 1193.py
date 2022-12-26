# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 20:24:08 2022

@author: kki
"""

# 1193번 분수찾기
# 큰 배열에 나열된 분수들을 1/1 -> 1/2 ->2/1 -> 3/1 -> 2/2 -> ... 과 같이 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, ..분수라고하자
# X가 주어졌을 대, X번째 분수를 구하는 프로그램을 작성하시오.

n = int(input())
line = 1

while n > line:
    n -= line  # 각 line에서 n이 몇번째에 위치하는지 알 수 있음
    line += 1
    
# line이 짝수일 때와 홀수일 대 분모 분자의 증감 양상이 다름
# 짝수일 때는 분모 -1, 분자 +1 씩, 홀수일 때는 분모 +1 씩, 분자 -1씩 증감함    
if line % 2 == 0:
    up = n
    down = line - n +1
else:
    up = line  -n + 1
    down = n

# 출력 시 sep = ""르 ㄹ써서 구분자를 변경해줌.    
print(up, '/', down, sep ="")
