# -*- coding: utf-8 -*-
# @Time    : 2020/2/5/005 16:48
# @Author  : mengchao
# @Site    : 
# @File    : Tree_Subtree.py
# @Software: PyCharm
"""
题目：树的子结构
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

解题：
1、在pRoot1中查找与根节点一样的值
2、判断pRoot1中以R为根节点的值是否与pRoot2具有相同的结构
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # 空树返回False
        if pRoot1 == None or pRoot2 == None:
            return False

        result1 = self.HasSubtree(pRoot1.left, pRoot2)  # 左子树
        result2 = self.HasSubtree(pRoot1.right, pRoot2) # 右子树
        result3 = self.isSubtree(pRoot1, pRoot2) # 对比函数

        if result1 == True or result2 == True or result3 == True:
            return True
        else:
            return False

    def isSubtree(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False

        if pRoot1.val == pRoot2.val:
            res1 = self.isSubtree(pRoot1.left, pRoot2.left)
            res2 = self.isSubtree(pRoot1.right, pRoot2.right)
            if res1 == True and res2 == True:
                return True
        return False
