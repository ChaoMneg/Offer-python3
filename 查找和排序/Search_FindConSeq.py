# -*- coding:utf-8 -*-
"""
题目：和为S的连续正数序列
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
"""
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        # 初始滑动窗口大小
        start = 1
        end = 2
        res = [] # 结果
        
        while start < end:
            # 计算滑动窗口的数值和大小
            cur_sum = sum(range(start, end+1))
            if cur_sum == tsum:
                res.append(range(start, end+1))
                end += 1
            elif cur_sum < tsum:
                end += 1
            else:
                start += 1
        return res
