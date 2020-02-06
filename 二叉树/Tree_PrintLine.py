# -*- coding: utf-8 -*-
# @Time    : 2020/2/6/006 13:27
# @Author  : mengchao
# @Site    : 
# @File    : Tree_PrintLine.py
# @Software: PyCharm
"""
题目：把二叉树打印成多行
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):

        if pRoot == None:
            return []

        queue1 = [pRoot]  # 队列，第一个为根节点
        queue2 = []
        ret = [] # 返回结果

        while queue1 or queue2:
            if queue1:  # 奇数行
                tmpRet = []  # 存放遍历的节点
                while queue1:
                    tmpNode = queue1[0]  # stack1 队列第一个数据
                    tmpRet.append(tmpNode.val) # 存取到值的值
                    del queue1[0] # 删除队列第一个数据
                    # 判断左右子树是否存在
                    if tmpNode.left:
                        queue2.append(tmpNode.left)  # 偶数行队列赋值
                    if tmpNode.right:
                        queue2.append(tmpNode.right)
                ret.append(tmpRet)

            if queue2: # 偶数行
                tmpRet = []
                while queue2:
                    tmpNode = queue2[0]
                    tmpRet.append(tmpNode.val)
                    del queue2[0]
                    if tmpNode.left:
                        queue1.append(tmpNode.left)
                    if tmpNode.right:
                        queue1.append(tmpNode.right)
                ret.append(tmpRet)
        return ret
