# -*- coding:utf-8 -*-
"""
题目：连续子数组的最大和
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和
"""
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        maxNum = None # 最大和
        tmpNum = 0
        for i in array:
            # 存入数组第一个值
            if maxNum == None:
                maxNum = i
            # 如果前(i-1)个数的和 < i, 那么舍弃前(i-1)个数，从i重新开始计数
            if tmpNum + i < i:
                tmpNum = i
            else:
                tmpNum += i
            # 判断是否为最大和
            if maxNum < tmpNum:
                maxNum = tmpNum
        return maxNum
