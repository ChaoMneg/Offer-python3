# -*- coding:utf-8 -*-
"""
题目：从上往下打印二叉树
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

思路：
1、使用两个list，其中ls存放二叉树的结点，result存放遍历后的结果
2、头结点添加完成后，将左右结点插入队列
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        # 获取头结点
        ls = [root]
        result = [] # 存放打印结果
        while len(ls) > 0:
            node = ls.pop(0)
            result.append(node.val)
            if node.left != None:
                ls.append(node.left)
            if node.right != None:
                ls.append(node.right)
        return result
