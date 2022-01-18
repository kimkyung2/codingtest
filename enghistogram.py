# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 10:26:27 2022

@author: kki
"""

def engfile(file_name):
    fr = open(file_name, 'rt', encoding = 'UTF-8')
    fr_msg = fr.read().lower()
    
    fr.close()
    
    
    
    Alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    fr_array = [0] * 26
    
    for ch in fr_msg:
        if ch in Alphabet:
            idx = Alphabet.find(ch)
            fr_array[idx] += 1
    
    for i in range(0, 26):
        print(Alphabet[i],'(',fr_array[i],') : ',fr_array[i]*'*' )
    
        
    
def test():
    print(' 영문 파일의 알파벳 수 구하기')
    
    engfile('eng.txt')

test()
