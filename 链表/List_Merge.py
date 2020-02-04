# -*- coding: utf-8 -*-
# @Time    : 2020/2/4/004 10:38
# @Author  : mengchao
# @Site    : 
# @File    : List_Merge.py
# @Software: PyCharm


"""
题目：合并两个排序的链表
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表

    # 递归
    def Merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1

        pHead = None  # 合并链表头结点
        if pHead1.val < pHead2.val:
            pHead = pHead1
            pHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pHead = pHead2
            pHead.next = self.Merge(pHead1, pHead2.next)
        return pHead
