# -*- coding:utf-8 -*-
"""
题目：数值的整数次方
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
"""
class Solution:
    def Power(self, base, exponent):
        flag = 0 # 指数为正
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if base == 0:
            return False
        if exponent < 0:
            flag = 1
        e = abs(exponent) # 取指数的绝对值
        res = 1
        for i in range(e):
            res = res * base 
        if flag == 1:
            res = 1 / res
        return res
