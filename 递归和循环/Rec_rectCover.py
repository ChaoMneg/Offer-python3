# -*- coding: utf-8 -*-
# @Time    : 2020/2/8/008 21:22
# @Author  : mengchao
# @Site    : 
# @File    : Rec_rectCover.py
# @Software: PyCharm
"""
题目：矩形覆盖
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

解法同青蛙跳台阶，f(n) = f(n-1) + f(n-2), f(1) = 1   f(2) = 2
"""
class Solution:
    def rectCover(self, number):
        res = [0,1,2]
        if number <= 2:
            return res[number]

        n1 = 2 # f(n-1)
        n2 = 1 # f(n-2)
        n = 0
        for i in range(3, number+1):
            n = n1 + n2
            n2 = n1
            n1 = n
        return n
