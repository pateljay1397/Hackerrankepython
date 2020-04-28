# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:07:41 2020

@author: patel
"""

if __name__ == '__main__':
    n = int(input())
    m = int(3*n)
    for i in range(0,int(n/2)):
        print(('.|.'*(2*i+1)).center(m,'-'))
    for i in range(1):
        print('WELCOME'.center(m,'-'))
    for i in range(int(n/2),0,-1):
        print(('.|.'*(2*i-1)).center(m,'-'))