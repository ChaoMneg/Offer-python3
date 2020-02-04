# -*- coding: utf-8 -*-
# @Time    : 2020/2/4/004 10:04
# @Author  : mengchao
# @Site    : 
# @File    : List_Reverse.py
# @Software: PyCharm


"""
题目：反转链表
输入一个链表，反转链表后，输出新链表的表头。

解题：
1、将头结点变为尾结点，指向None
2、从第二个节点开始循环指向前一个节点
3、需要一个指针指向还没翻转的节点
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # 空链表
        if pHead == None:
            return None
        # 单节点
        if pHead.next == None:
            return pHead

        last = None
        while pHead:
            rawList = pHead.next  # 存储截断后的原始链表
            pHead.next = last # 链表翻转
            last = pHead # 获取翻转的尾节点
            pHead = rawList # 获取翻转的头节点
        return last
