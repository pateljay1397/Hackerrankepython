# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 02:44:02 2020

@author: patel
"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m = max(arr)
    i=0
    while(n>i):
        if m==max(arr):
            arr.remove(m)
        i+=1
    print(max(arr))