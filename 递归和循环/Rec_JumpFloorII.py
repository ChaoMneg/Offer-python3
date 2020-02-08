# -*- coding: utf-8 -*-
# @Time    : 2020/2/8/008 21:11
# @Author  : mengchao
# @Site    : 
# @File    : Rec_JumpFloorII.py
# @Software: PyCharm
"""
题目：青蛙跳台阶Ⅱ
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
f(n) = 2^(n-1)
"""
class Solution:
    def jumpFloorII(self, number):
        if number <= 0:
            return 0
        else:
            return pow(2, number-1)
