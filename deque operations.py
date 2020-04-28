# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:26:48 2020

@author: patel
"""
from collections import deque
d = deque()
for _ in range(int(input())):
    method,*number = input().split()
    if(method=="append"):
        d.append(number[0])
    elif(method=="appendleft"):
        d.appendleft(number[0])
    elif(method=="pop"):
        d.pop()
    else:
        d.popleft()
print(*[item for item in d])