# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:24:27 2020

@author: patel
"""
if __name__ == '__main__':
    n = int(input())
    words = input().split(" ")
    words1 = [] 
    [words1.append(words[i]) for i in range(n) if words[i] not in words1]
    print(len(words1))
    for i in range(len(words1)):
        counter = words.count(words[i])
        print(counter,end=" ")
        