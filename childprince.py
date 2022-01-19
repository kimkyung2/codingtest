# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:07:23 2022

@author: -
"""
Tcases = int(input())
results = []

def prince(Tcases):

    for case in range(Tcases):
        count = 0
        x1, y1, x2, y2 = map(int,input().split())
        pnumber = int(input())
        planets = []
        
        for p in range(pnumber):
            px, py, pr = map(int, input().split())
            d1 = (x1-px)**2 + (y1-py)**2 
            d2 = (x2-px)**2 + (y2-py)**2
            
            if d1 <pr**2 or d2<pr**2:
                if d1 < pr**2 and d2 <pr**2:
                    pass
                else:
                    count += 1  
        results.append(count)

def result(results):
    for i in results:
        print(i)
    
    
def test():
    
    prince(Tcases)
    result(results)
test()