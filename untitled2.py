# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 01:09:27 2020

@author: patel
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    Query_name = input()
    if Query_name in student_marks.keys():
        print(round(sum(student_marks[Query_name])/3.0),2)