# -*- coding: utf-8 -*-
# @Time    : 2020/2/5/005 15:47
# @Author  : mengchao
# @Site    : 
# @File    : Tree_Symmetrical.py
# @Software: PyCharm

"""
题目：对称的二叉树
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    # 判断函数
    def isSame(self, pRoot1, pRoot2):

        # 特殊情况
        if pRoot1 == None and pRoot2 == None:
            return True
        if pRoot1 == None or pRoot2 ==None:
            return False
        if pRoot1.val != pRoot2.val:
            return False

        # 判断pRoot1的左子树与pRoot2的右子树是否相同
        left = self.isSame(pRoot1.left, pRoot2.right)
        if not left:
            return False
        # 判断pRoot1的右子树与pRoot2的左子树是否相同
        right = self.isSame(pRoot1.right, pRoot2.left)
        if not right:
            return False
        return True
    def isSymmetrical(self, pRoot):
        return self.isSame(pRoot, pRoot)

