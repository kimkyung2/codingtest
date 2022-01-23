# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:37:05 2022

@author: quffh
"""

# 개똥벌레
# 개동벌레가 파괴해야하는 장애물의 최솟값과 구간이 총 몇개 인지 구하기
# 조건
# 1. 길이 : N미터(짝수), 높이 : H미터
# 2. 첫번째 장애물은 항상 석순, 그 이후는 종유석과 석순 벌갈아 등장
# 3. 장애물의 크기는 H보다 작은 양수

# 풀이 : 누적합을 사용한다
# 특정 높이 H에서 지나가는 종유석의 개수는 높이 H+1 에서 
# 통과하는 종유석의 개수 + 높이 H에서 새롭게 통과하는 종유석의 개수로 판단 가능

if __name__ == '__main__':
    N, H = map(int, input().split())
    top = [0] * (H+1) # 종유석
    bottom = [0] * (H+1) # 석순
    
    for i in range(N):
        num = int(input())
        if i % 2: 
            top[num] += 1
        else: 
            bottom[H - num +1] += 1
    
    for i in range(H-1, 0, -1):
        top[i] += top[i +1]
    
    for i in range(1, H+1):
        bottom[i] += bottom[i-1]
    total = [0] * (H+1)
    
    for i in range(1, H+1):
        total[i] = top[i] + bottom[i]
    
    total = total[1:]
    ans = min(total)
    print(ans, total.count(ans))
            
            