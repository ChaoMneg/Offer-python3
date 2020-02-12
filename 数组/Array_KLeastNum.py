# -*- coding:utf-8 -*-
"""
题目：最小的K个数
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

备注：不是最优解，其他方法没搞明白
"""
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput == [] or k > len(tinput):
            return []
        tinput.sort()
        return tinput[:k]
