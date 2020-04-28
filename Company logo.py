# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:52:06 2020

@author: patel
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        prev = None
        temp= None
        carry= 0
        while l1 is not None or l2 is not None:
            fdata=0 if l1 is None else l1.data
            sdata=0 if l2 is None else l2.data
            s =sum(carry+fdata+sdata)
            carry=1 if s>10 else 0
            s=s if s<10 else s%10
            temp = Node(s)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
