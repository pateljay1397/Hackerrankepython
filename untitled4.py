# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 17:12:18 2020

@author: patel
"""
def minion_game(string):
    staurt=0
    kevin=0
    for i in range(0,len(string)):
        if string[i] in ['A','E','I','O','U']:
            kevin +=(len(string)-i)
        else :
            staurt +=(len(string)-i)
    if staurt>kevin:
        print("Stuart",staurt)
    elif kevin>staurt:
        print("Kevin",kevin)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)