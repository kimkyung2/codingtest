# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 11:04:44 2022

@author: kki
"""
import math, sys, itertools

Tcases = int(input())
 
for test_case in range(Tcases):
    n = int(input())
    point = []
    total_x = 0
    total_y = 0
    
    for _ in range(n):
        x, y = list(map(int, input().split()))
        point.append([x, y])
        total_x += x
        total_y += y
        
    ret = sys.maxsize
    com = list(itertools.combinations(point, int(n/2)))
    com_len = int(len(com)/2)
    
    for element in com[:com_len]:
        element = list(element)
        
        x1_total = 0
        y1_total = 0
        
        for x1, y1 in element:
            x1_total += x1
            y1_total += y1
            
        x2_total = total_x - x1_total
        y2_total = total_y - y1_total
        
        ret = min(ret, math.sqrt((x1_total - x2_total)**2 + (y1_total - y2_total)**2))
    print(ret)