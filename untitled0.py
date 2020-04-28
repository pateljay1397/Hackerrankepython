# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 01:14:10 2020

@author: patel
"""
def print_formatted(number):
    # your code goes here
    w = len(bin(number)[2:])
    for i in range(1,n+1):
        print(i,oct(i).replace('0o','').rjust(w),hex(i).replace('0x','').capitalize().rjust(w),bin(i).replace('0b','').rjust(w))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)