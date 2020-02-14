# -*- coding:utf-8 -*-
"""
题目：和为S的两个数字
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

思路：两个指针，一个指向头结点，一个指向尾结点
"""
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) < 1:
            return []
        # 定义开始结束结点
        start = 0
        end = len(array)-1
        while start < end:
            # 两个结点的和
            cur_sum = array[start] + array[end]
            if cur_sum == tsum:
                return [array[start], array[end]]
            elif cur_sum > tsum:
                end -= 1
            else:
                start += 1
        return []
