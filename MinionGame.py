# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:33:58 2020

@author: patel
"""
def minion_game(string):
    staurt=0
    kevin=0
    res = string
    for i in range(0,len(res)):
        if res[i] in ['A','E','I','O','U']:
            kevin = string.count(res[i],0,len(string))
            kevin +=kevin
        else :
            staurt = string.count(res[i],0,len(string))
            staurt +=staurt
    if staurt>kevin:
        print("Stuart",staurt)
    else:
        print("Kevin",kevin)
if __name__ == '__main__':
    s = input()
    minion_game(s)