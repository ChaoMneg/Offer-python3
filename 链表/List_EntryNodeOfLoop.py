# -*- coding: utf-8 -*-
# @Time    : 2020/2/3/003 18:43
# @Author  : mengchao
# @Site    : 
# @File    : List_EntryNodeOfLoop.py
# @Software: PyCharm

"""
题目：链表中环的入口结点
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # 如果链表为空
        if pHead == None:
            return None

        # 定义两个指针
        fast = pHead
        slow = pHead
        # fast当前节点与下一个节点不为None
        while fast and fast.next:
            fast = fast.next.next # fast前进两步
            slow = slow.next # slow前进一步
            # fast == slow存在环
            if fast == slow:
                pTmp = pHead
                # 下一个相遇节点即为环入口节点
                while pTmp != slow:
                    pTmp = pTmp.next
                    slow = slow.next
                return slow
