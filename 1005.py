# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:59:54 2022

@author: kki
"""

# 1005번 ACM Craft
# 이 게임은 건물을 짓는 순서가 정해져 있지 않음
# 첫번째 게임과 두번째 게임이 건물을 짓는 순서가 다를 수 있음
# 매 게임시작 시 건물을 짓는 순서가 주어짐, 모든 건물은 각각 건설하여 완성이 될 때까지 delay가 존재
# 특정건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내는 프로그램

T = int(input())
results = []

for _ in range(T):
    n, k = map(int, input().split()) # 건물수와 건설순서 규칙의 총 개수 
    d = list(map(int, input().split())) # 건물당 걸설에 걸리는 시간
    
    R = [] # 건설순서 x, y
    for i in range(k):    
        x, y = map(int, input().split())
        R.append([x,y])
    
    W = int(input()) # 건설해야할 건물의 번호
    
    # 잔여 시간 정보 : 각 건물의 잔여시간을 기록하는 dict
    # 이 변수는 매 최소시간이 흐를 때마다 갱신되고, value가 0이되면 완성된 건물로 판단함
    operating_map = {}
    for building, time in enumerate(d):
        operating_map[building + 1] = time
        
    # 각 건물의 선행 건물에 대한 정보 : 진입 차수가 0인 건물과 선행 건물이 요구되는 건물들의 정보가 저장된 dict
    # 1번 건물은 선행 건물이 없으므로, 초기 건물로 생각할 수 있다.
    # 이 변수는 매 건물이 완성 될때마다, 완성된 건물의 set이 남은 건물들의 선행 건물 set을 포함하고 있을 때 그 건물은 건설시작이 가능함을 아렬줄 수 있음
    rule_map = {}
    for i in range(n):
        rule_map[i+1] = set()
    for rule in R:
        x = rule[0]
        y = rule[1]
        rule_map[y].add(x)
    
    # 완성된 건물
    done = set()
    time = 0
    
    # 목표 건물 w가 완료된 건물에 포함될 때 까지
    while W not in done:
        # 건설 진행중인 건물들
        bases = []
        for building in rule_map:
            # 잔여 건물 중, 선행건물들이 모두 완료되었을 경우 건설 중인 건물에 추가
            if done.issuperset(rule_map[building]) and building not in done:
                bases.append(building)
            
        # 건설 중인 건물 중 잔여 최소 시간 계산 후, 총 시간에 더함
        time_step = min([operating_map[base] for base in bases])
        time += time_step
        
        # 건설 잔여 시간 갱신
        for base in bases:
            operating_map[base] -= time_step
            # 잔여 시간이 0일 경우 done에 추가
            if operating_map[base] == 0:
                done.add(base)
                
    results.append(time)

for result in results:
    print(str(result))
    
    