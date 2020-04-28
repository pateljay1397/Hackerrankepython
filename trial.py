# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 17:25:56 2020

@author: patel
"""
import string 
if __name__ == '__main__':
    n = int(input())
    L= list()
    L1=list()
    alpha = string.ascii_lowercase
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append(s[::-1]+s[1:])
    length = len(L[0])
    for i in range(n-1,0,-1):
        print(L[i].center(length,'-'))
    for i in range(n):
        print(L[i].center(length,'-'))