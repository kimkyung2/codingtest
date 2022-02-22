# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:24:03 2022

@author: kki
"""

# 2839번 설탕 배달
# 설탕 봉지는 3킬로그램과 5킬로그램 봉지가 있음
# N 킬로그램을 배달해야할 때 더 적은 개수의 봉지를 배달해야 함
# 상근이가 배달하는 봉지의 최소 개수를 출력하고, 정확하게 N킬로그램을 만들 수 없다면 -1을  출력

sugar = int(input())
cnt = 0

while sugar >= 0:
    if sugar % 5 == 0:
        cnt += (sugar // 5)
        print(cnt)
        break
    sugar -= 3
    cnt += 1
else:
    print(-1)

        
        