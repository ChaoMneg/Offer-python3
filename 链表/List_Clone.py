# -*- coding: utf-8 -*-
# @Time    : 2020/2/4/004 11:23
# @Author  : mengchao
# @Site    : 
# @File    : List_Clone.py
# @Software: PyCharm

"""
题目：复杂链表的复制
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

思路：
1、复制原始链表中的每个节点，并将其安装A -> A' -> B -> B'的形式链接
2、复制random链接S，复制链接为S'= S.next
3、按奇偶位置拆除链表，偶数为复制链接
"""

# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        pNode = pHead
        # 复制节点，并链接成A -> A' -> B -> B'的形式
        while pNode != None:
            pClone = RandomListNode(pNode.label)  # 复制节点A'
            pClone.next = pNode.next # A' -> B
            pNode.next = pClone # A -> A'
            pNode = pClone.next # 获取下一个节点B

        self.ConnectSiblingNodes(pHead)  # 复制random链接
        pCloneHead = self.ReconnectNodes(pHead)  # 拆分复制链表
        return pCloneHead

    # 复制random链接
    def ConnectSiblingNodes(self,pHead):
        pNode = pHead
        while pNode != None:
            pClone = pNode.next # 获取第一个复制节点A'
            if pNode.random != None:  # 判断节点是否有随机链接
                pClone.random = pNode.random.next # 复制随机链接
            pNode = pClone.next

    # 拆分原始链表与复制链表
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pCloneHead = None  # 复制链表的头结点
        pCloneNode = None

        # 执行一次，将第一个节点链接断开
        if pNode != None:
            pCloneHead = pCloneNode = pNode.next # 获取复制链表的头节点A'
            pNode.next = pCloneNode.next # 将 A 重新链接到 B
            pNode = pNode.next # 获取B

        while pNode != None:
            pCloneNode.next = pNode.next # 执行A'->B'
            pCloneNode = pCloneNode.next # 获取B'
            pNode.next = pCloneNode.next # B -> C
            pNode = pNode.next # 获取C
        return pCloneHead
