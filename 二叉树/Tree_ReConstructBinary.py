# -*- coding: utf-8 -*-
# @Time    : 2020/2/5/005 11:07
# @Author  : mengchao
# @Site    : 
# @File    : Tree_ReConstructBinary.py
# @Software: PyCharm

"""
题目：
重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

思路：
1、前序遍历第一个节点为根节点
2、中序遍历中找到根节点的index，根据index拆分左右子树
3、递归循环
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])  # 根节点的值
        pos = tin.index(pre[0]) # 根节点在中序遍历中的位置

        preLeft = pre[1:pos+1]  # 前序-左子树（pos+1取不到，取的1-pos）
        preRight = pre[pos+1:] # 前序-右子树
        tinLeft = tin[:pos] # 中序-左子树
        tinRight = tin[pos+1:] # 中序-右子树
        # 递归
        root.left = self.reConstructBinaryTree(preLeft, tinLeft)
        root.right = self.reConstructBinaryTree(preRight, tinRight)
        return root

s = Solution()
pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
res = s.reConstructBinaryTree(pre, tin)
print(res.val)
