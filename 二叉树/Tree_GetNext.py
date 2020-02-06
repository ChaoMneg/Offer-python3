# -*- coding: utf-8 -*-
# @Time    : 2020/2/5/005 14:38
# @Author  : mengchao
# @Site    : 
# @File    : Tree_GetNext.py
# @Software: PyCharm
"""
题目：二叉树的下一个结点
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

解题：
1、寻找右子树，如果存在就寻找右子树的最左子树
2、没有右子树，寻找该节点的父节点，判断找到的节点是否是父节点的左子树，如果是打印父节点
"""
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if pNode.right: # 如果存在右子树
            tmpNode =  pNode.right
            while tmpNode.left:
                tmpNode = tmpNode.left  # 寻找左子树
            return tmpNode
        else:
            tmpNode = pNode
            while tmpNode.next: # 寻找父节点
                if tmpNode.next.left == tmpNode:
                    return tmpNode.next
                tmpNode = tmpNode.next
            return None
