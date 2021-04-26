# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:24:31 2020

@author: HallJ
"""


values = {'a': 2, 'b': 3, 'c':5, 'd':7, 'e':11, 'f':13, 'g':17,
          'h': 19, 'i':23, 'j':27, 'k': 29, 'l':31}

def computevalues(sample, text):
    anaValue = [1]*(len(text) - len(sample))
    Target = 1
    for c in sample:
        Target *= values[c]
    for i in range(len(sample)):
        
        anaValue[0] *= values[text[i]]
        
    for i in range(1,len(text)-len(sample)):      
        anaValue[i] = (anaValue[i-1] // values[text[i-1]]) * values[text[i+len(sample)-1]]
        print(anaValue[i])
    print(anaValue)
    print(Target)
    
    
computevalues('abbacab', 'adabcbabababfgebcabcabcabcabcacbbcbakababa')    