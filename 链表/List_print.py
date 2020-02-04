# -*- coding: utf-8 -*-
# @Time    : 2020/2/3/003 15:31
# @Author  : mengchao
# @Site    : 
# @File    : List_print.py
# @Software: PyCharm

# -*- coding:utf-8 -*-
"""
题目：从尾到头打印链表
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""

# 创建链表节点
class ListNode:
    def __init__(self, x):
        self.val = x  # 值
        self.next = None # 下一个节点

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        l = []  # 结果存储的list
        head = listNode # 获取链表的头节点
        while head:
            l.insert(0, head.val) # 将节点值存储在list的头部（0），每次都存在头部
            head = head.next # 获取下一个节点
        print(l)
        return l

# 创建链表
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = None

# 测试函数
s = Solution()
a = s.printListFromTailToHead(l1)
