# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 14:01:41 2022

@author: quffh
"""

# 1946번 신입사원
# 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발
# 어던 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 
# 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않음
# 조건을 만족시키면서 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원 수 구하기

# 입력 : 서류심사 성적, 면접 성적의 순위
# 하나를 기준으로 정렬을 하고, 나머지 하나의 순위만 놓고 비교하면 됨

T = int(input())

for i in range(T):
    person = []
    N = int(input())
    
    for j in range(N):
        paper, interview = map(int, input().split())
        person.append([paper, interview])
        
    person.sort() # 서류 성적순으로 오름차순 정렬
    tmp = person[0][1]
    cnt = 1
    
    for j in range(1,N):
        if tmp > person[j][1]:
            cnt += 1
            tmp = person[j][1]
    print(cnt)
            