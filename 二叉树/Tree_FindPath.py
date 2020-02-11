# -*- coding:utf-8 -*-
"""
题目：二叉树中和为某一值的路径
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

思路：
1、递归先序遍历树， 把结点加入路径。
2、若该结点是叶子结点则比较当前路径和是否等于期待和。
3、弹出结点，每一轮递归返回到父结点时，当前路径也应该回退一个结点

"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def FindPath(self, root, expectNumber):
        def subFindPath(root):
            if root:
                b.append(root.val) # 根结点值
                if not root.right and not root.left and sum(b) == expectNumber:
                    a.append(b[:]) # 深拷贝
                else:
                    subFindPath(root.left),subFindPath(root.right)
                b.pop()
        a, b = [], []
        subFindPath(root)
        return a
