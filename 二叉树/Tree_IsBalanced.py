# -*- coding:utf-8 -*-
"""
题目：平衡二叉树
输入一棵二叉树，判断该二叉树是否是平衡二叉树。（任意结点左右子树深度不超过1）

"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 判断二叉树深度
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        return max(self.TreeDepth(pRoot.left)+1, self.TreeDepth(pRoot.right)+1)
    
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        
        diff = abs(left - right)
        if diff <= 1:
            return True
