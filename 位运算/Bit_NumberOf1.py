# -*- coding:utf-8 -*-
"""
题目：二进制中1的个数
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

解题：
n-1与n做&运算后，会把最右边的1变为0，重复操作即可得到1的个数
"""
class Solution:
    def NumberOf1(self, n):
        count = 0
        # 获取负数的补码
        if n < 0:
            n = n & 0xffffffff
        while n:
            count = count + 1
            n = n & (n-1) # 与运算，0&0=0;0&1=0;1&0=0;1&1=1;
        return count
