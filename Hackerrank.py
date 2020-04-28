# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 01:20:02 2020

@author: patel
"""



def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        if(year%100==0):
            if(year%400==0):
                leap=True
            else:
                leap=False
        else:
            leap=True
    return leap

year = int(input())
print(is_leap(year))