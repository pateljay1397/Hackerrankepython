# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:41:05 2020

@author: patel
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    student_data = [" "," "," "]
    for i in range(0,n):
        student_name = input()
        student_marks[student_name]={}
        for entry in student_data:
            student_marks[student_name][entry]=float(input(entry))
    Query_name = input()
    average = 0
    if Query_name in student_marks.keys():
        print (str(sum(student_marks[Query_name].values())/3.0))