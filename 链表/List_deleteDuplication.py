# -*- coding: utf-8 -*-
# @Time    : 2020/2/4/004 15:56
# @Author  : mengchao
# @Site    : 
# @File    : List_deleteDuplication.py
# @Software: PyCharm

"""
题目：删除链表中重复的结点
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        if pHead == None or pHead.next == None:
            return pHead

        Head = ListNode(0)  # 创建头节点
        Head.next = pHead
        pre = Head
        last = Head.next
        while last != None:
            if last.next != None and last.val == last.next.val:  # 如果两个节点相等
                # 一直循环，直至不相等
                while last.next != None and last.val == last.next.val:
                    last = last.next
                pre.next = last.next # 删除重复节点
                last = last.next
            else:
                pre = pre.next
                last = last.next
        return Head.next

