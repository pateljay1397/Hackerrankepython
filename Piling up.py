# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:16:15 2020

@author: patel
"""
from collections import deque
for _ in range(int(input())):
    n = int(input())
    length = deque(input().split())
    result = "Yes"
    if max(length) not in (length[0],length[-1]):
        result="No"
    print(result)