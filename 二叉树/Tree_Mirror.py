# -*- coding: utf-8 -*-
# @Time    : 2020/2/5/005 15:55
# @Author  : mengchao
# @Site    : 
# @File    : Tree_Mirror.py
# @Software: PyCharm

"""
题目：二叉树的镜像
操作给定的二叉树，将其变换为源二叉树的镜像。
二叉树的镜像定义：
         源二叉树
    	     8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11

    	镜像二叉树
    	     8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root == None:
            return None

        if root.left == None and root.right == None:
            return None

        # 交换根节点的左右节点
        tmpNode = root.left
        root.left = root.right
        root.right = tmpNode

        # 执行迭代
        if root.left:
            self.Mirror(root.left)

        if root.right:
            self.Mirror(root.right)
