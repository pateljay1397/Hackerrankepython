# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:23:27 2020

@author: patel
"""

n = int(input())
s_info = {}
for i in range(n):
    s_name, *line = input().split() 
    scores = list(map(float,line))
    s_info[s_name] = scores

print(s_info)
q_name = input()
if q_name in s_info.keys():
    print(s_info[q_name])
    marks = sum({}.fromkeys(['q_name'].value(), 0))
    print(marks)
    
    