# -*- coding:utf-8 -*-
"""
题目：二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

思路：
1、获取根结点
2、根结点应 > 所有左子树的结点值
3、根结点应 < 所有右子树的结点值
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        length = len(sequence)
        if length <= 0:
            return False
        root = sequence[-1]
        
        # 获取左子树index
        for i in range(length):
            if sequence[i] > root:
                break
        while i < length-1:
            if sequence[i] < root:
                return False
            i += 1
        # 存储左右子树
        left = sequence[: i]
        right = sequence[i: length-1]
        
        leftIs = True
        rightIs = True
        
        if len(left) > 0:
            leftIs = self.VerifySquenceOfBST(left)
        if len(right) > 0:
            rightIs = self.VerifySquenceOfBST(right)
        return leftIs & rightIs
            
