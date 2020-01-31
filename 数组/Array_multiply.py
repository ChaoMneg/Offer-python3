# -*- coding: utf-8 -*-
# @Time    : 2020/1/31/031 16:40
# @Author  : mengchao
# @Site    :
# @File    : Array_multiply.py
# @Software: PyCharm

"""
题目：乘积数组
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。
"""


class Solution:
    def multiply(self, A):
        if not A:
            return False

        n = len(A)
        B = [None] * n
        B[0] = 1

        # 前半部分，从上往下计算
        for i in range(1, n):
            B[i] = B[i-1] * A[i-1]

        # 后半部分，从下往上计算
        tmp = 1
        for j in range(n-2, -1, -1):
            tmp = tmp * A[j+1]
            B[j] = B[j] * tmp
        return B

S = Solution()
A = [2,3,4,5,6]
B = S.multiply(A)
print(B)

