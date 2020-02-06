# -*- coding: utf-8 -*-
# @Time    : 2020/2/6/006 12:56
# @Author  : mengchao
# @Site    : 
# @File    : Tree_Print.py
# @Software: PyCharm
"""
题目：按之字形顺序打印二叉树
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

解题：
1、两个list分别存放奇数行跟偶数行
2、奇数行从左到右
3、偶数行从右到左
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):

        if pRoot == None:
            return []

        stack1 = [pRoot]  # 堆栈，第一个为根节点
        stack2 = []
        ret = [] # 返回结果

        while stack1 or stack2:
            if stack1:  # 奇数行
                tmpRet = []  # 存放遍历的节点
                while stack1:
                    tmpNode = stack1.pop()  # stack1 堆栈弹出数据
                    tmpRet.append(tmpNode.val) # 存放弹出的数据
                    # 判断左右子树是否存在
                    if tmpNode.left:
                        stack2.append(tmpNode.left)  # 堆栈先进后出，偶数行从右向左遍历所以先放左子树
                    if tmpNode.right:
                        stack2.append(tmpNode.right)
                ret.append(tmpRet)

            if stack2: # 偶数行
                tmpRet = []
                while stack2:
                    tmpNode = stack2.pop()
                    tmpRet.append(tmpNode.val)
                    if tmpNode.right:
                        stack1.append(tmpNode.right)
                    if tmpNode.left:
                        stack1.append(tmpNode.left)
                ret.append(tmpRet)
        return ret
