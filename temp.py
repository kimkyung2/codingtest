# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

data = []

for i in range(10):
    num = random.randrange(1, 1000000)
    data.append(num)
print(data)    

def bubble(n):
    for i in range(len(n)):
        for j in range(len(n)-1):
            if n[j] < n[j+1]:
                (n[j], n[j+1]) = (n[j+1],n[j])
        # print('i = ', i, 'j = ', data)
    print(n) 
# bubble(data)

def bubble_recursive(n):
    for i in range(len(n)-1):
        if n[i] < n[i+1]:
            a = n[i]
            n[i] = n[i+1]
            n[i+1] = a
            bubble_recursive(n)
            
    return n
# print(bubble_recursive(data))

def quick(array):
    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2]
    leftside, rightside, equal = [], [], []
    
    for num in array:
        if num < pivot:
            leftside.append(num)
        elif num > pivot:
            rightside.append(num)
        else:
            equal.append(num)
    
    return quick(leftside) + equal + quick(rightside)

def select(a):
    n = len(a)
    for i in range(0, n-1):
        max_idx = i
        for j in range(i+1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
# select(data)
# print(data)

def select_recursive(ulist):
    olist = []
    if ulist != []:
        x = max(ulist)
        olist = [x]
        ulist.remove(x)
        return olist + select_recursive(ulist)
    else:
        return []

def test():
    # bubble(data)
    # print(bubble_recursive(data))
    # select(data)
    # print(data)
    # print(select_recursive(data))
    print(quick(data))
    
test()