# -*- coding: utf-8 -*-
# @Time    : 2020/2/6/006 15:35
# @Author  : mengchao
# @Site    : 
# @File    : Tree_KthNode.py
# @Software: PyCharm

"""
题目：二叉搜索树的第k个结点
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

二叉搜索树：
1、它或者是一棵空树，
2、若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
3、若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；

解题：
使用中序遍历后，list从小到大排序
"""

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if pRoot == None:
            return None
        res = self.MidNode(pRoot)
        if k <= 0 or len(res) < k:
            return None
        else:
            return res[k-1]

    # 中序遍历
    def MidNode(self, root):
        res = []
        if root == None:
            return None
        if root.left:
            res.extend(self.MidNode(root.left))
        res.append(root)
        if root.right:
            res.extend(self.MidNode(root.right))
        return res


