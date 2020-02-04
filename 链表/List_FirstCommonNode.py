# -*- coding: utf-8 -*-
# @Time    : 2020/2/4/004 13:09
# @Author  : mengchao
# @Site    : 
# @File    : List_FirstCommonNode.py
# @Software: PyCharm

"""
题目：两个链表的第一个公共结点
输入两个链表，找出它们的第一个公共结点。
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:

    # 发现公共节点
    # short：短链表   long：长链表   sHead：短链表头节点   lHead：长链表头节点
    def find(self, short, long, sHead, lHead):
        k = 0
        # 发现两个链表长度的差k
        while long:
            long = long.next
            k = k + 1
        short = sHead
        long = lHead
        # 长链表先走k步
        for i in range(k):
            long = long.next
        # 找公共节点
        while short != long:
            short = short.next
            long = long.next
        return short


    def FindFirstCommonNode(self, pHead1, pHead2):
        p1 = pHead1
        p2 = pHead2

        # 求两个链表的长度，长度不同时，先遍历完一个链表
        while p1 and p2:
            if p1 == p2:  # 两个链表为空时
                return p1
            p1 = p1.next
            p2 = p2.next

        # 如果p1为长链表
        if p1:
            return self.find(p2, p1, pHead2, pHead1)
        # 如果p2为长链表
        if p2:
            return self.find(p1, p2, pHead1, pHead2)
