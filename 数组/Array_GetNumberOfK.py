# -*- coding:utf-8 -*-
"""
题目：数字在排序数组中出现的次数
统计一个数字在排序数组中出现的次数。

思路：二分查找

"""
class Solution:
    def GetNumberOfK(self, data, k):
        start = 0 # 头指针
        end = len(data) - 1 # 尾部指针
        kIndex = -1  # k的索引
        # 使用二分查找
        while start <= end:
            mid = (start+end) >> 1 # /2
            if data[mid] == k:
                kIndex = mid
                break
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        if kIndex == -1:
            return 0
        # 找到k后，继续向k的前后查找
        start1 = kIndex - 1
        end1 = kIndex + 1
        count = 1
        while (start1 >= 0) and (data[start1]) == k:
            start1 = start1 - 1
            count += 1
        while (end1 <= len(data) - 1) and (data[end1]) == k:
            end1 = end1 + 1
            count += 1
        return count
