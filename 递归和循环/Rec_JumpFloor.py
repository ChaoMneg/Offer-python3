# -*- coding: utf-8 -*-
# @Time    : 2020/2/8/008 20:07
# @Author  : mengchao
# @Site    : 
# @File    : Rec_JumpFloor.py
# @Software: PyCharm

"""
题目：青蛙跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
斐波那契数列：1, 2, 3, 5, 8.....
"""

class Solution:
    def jumpFloor(self, number):
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

# 测试
s = Solution()
print(s.jumpFloor(4))
