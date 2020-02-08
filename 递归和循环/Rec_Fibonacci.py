# -*- coding: utf-8 -*-
# @Time    : 2020/2/8/008 19:16
# @Author  : mengchao
# @Site    : 
# @File    : Rec_Fibonacci.py
# @Software: PyCharm

"""
题目：斐波那契数列
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

0、1、1、2、3、5、8、13、21、34、……
"""
class Solution:
    def Fibonacci(self, n):
        res = [0,1]
        if n < 2:
            return res[n]

        fibNMinusOne = 1 # f(n-1)
        fibNMinusTwo = 0 # f(n-2)
        fibN = 0
        for i in range(2, n+1):
            fibN = fibNMinusOne + fibNMinusTwo # f(n) = f(n-1) + f(n-2)
            fibNMinusTwo = fibNMinusOne
            fibNMinusOne = fibN
        return fibN

# 测试
s = Solution()
print(s.Fibonacci(2))




