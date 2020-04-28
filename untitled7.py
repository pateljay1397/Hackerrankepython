# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:13:03 2020

@author: patel
"""

s = input()
for i in s[:].split():
    s = s.replace(i, i.capitalize())
print(s)