# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:05:31 2022

@author: kki
"""

# 1475번 방번호
# 플라스틱 숫자를 한 세트로 팔 때, 한세트에는 0 ~ 9까지 숫자가 하나씩 들어있다.
# 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오.
# 6은 9룰 뒤집어서, 9는 6을 뒤집어서 이용할 수 있다.

n = input()

cnt = [0] * 10 # 0~9까지의 번호를 넣을 수 있는 list 생성

for i in n: 
    index = int(i) # 문자열로 입력받았으니 숫자로 변경
    if index == 9 or index == 6: # 6이랑 9는 뒤집어서 사용할 수 있기 때문에 둘 중 하나가 나오면
        cnt[6] += 1 # 6 에 1을 더해둔다
    else:
        cnt[index] += 1 # 아니면 해당되는 숫자에 1을 더함
        
if cnt[6] % 2 == 0: 
    cnt[6] = cnt[6] //2 # 6과 9의 개수를 더한 값이 짝수라면 몫을 넣고
else:
    cnt[6] = (cnt[6]//2) + 1 # 아니라면 몫에 1을 더해줌.
    
print(max(cnt)) # 값중에서 가장 큰 값을 출력
        
        




