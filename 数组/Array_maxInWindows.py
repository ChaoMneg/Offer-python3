# -*- coding: utf-8 -*-
# @Time    : 2020/2/7/007 13:39
# @Author  : mengchao
# @Site    : 
# @File    : Array_maxInWindows.py
# @Software: PyCharm

"""
题目：滑动窗口的最大值
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
"""

class Solution:
    def maxInWindows(self, num, size):
        if size <= 0:
            return []

        res = []
        for i in range(len(num)-size+1):
            res.append(max(num[i:i+size]))
        return res
