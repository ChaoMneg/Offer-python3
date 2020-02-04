# -*- coding: utf-8 -*-
# @Time    : 2020/2/3/003 17:12
# @Author  : mengchao
# @Site    : 
# @File    : List_FindKthToTail.py
# @Software: PyCharm
"""
题目：链表中倒数第k个结点
输入一个链表，输出该链表中倒数第k个结点。

解题：
因为是单链表，所以倒数第K个节点是正数第n-(k+1)个节点；
设置两个指针，p1，p2，先让p2走k-1步，然后再一起走，直到p2为最后一个 时，p1即为倒数第k个节点
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        p1 = head
        p2 = head

        # 特殊情况直接返回False
        if head == None or k <= 0:
            return None

        # p2走k-1步
        while k > 1:
            if p2.next != None:
                p2 = p2.next
                k = k -1
            else:
                return None

        # 两个一起走
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        print(p1.val)  # 测试
        return p1



# 创建链表
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = None

s = Solution()
s.FindKthToTail(l1,3)
