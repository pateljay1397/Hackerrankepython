# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 02:03:59 2020

@author: patel
"""
if __name__ == '__main__':
    arr1=[]
    n=int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        arr = [name , score]
        arr1.append(arr)
        m=min(arr1,key= lambda x:x[1])
    i=0
    while(n>i):
        if m==min(arr1,key= lambda x:x[1]):
            arr1.remove(m)
        i+=1    
        print(min(arr1,key= lambda x:x[1])) 