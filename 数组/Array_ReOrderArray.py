# -*- coding:utf-8 -*-
"""
题目：调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

思路1：两个指针一个分别从首、尾开始遍历，Start指针遇到偶数，End遇到奇数时交换两个数(剑指Offer版本)
思路2：
"""
class Solution:
    # 剑指Offer版本，不能满足奇数和奇数，偶数和偶数之间的相对位置不变
    def reOrderArray(self, array):
        length = len(array)
        if length == 0:
            return None
        Start = 0
        End = length - 1
        while Start < End:
            while (Start < End) and (array[Start]%2 == 1):
                Start = Start + 1
            while (Start < End) and (array[End]%2 == 0):
                End = End - 1
                
            if Start < End:
                array.insert(Start,array.pop(End))
        return array
      
    # 思路2：直接遍历数组
    def reOrderArray(self, array):
        length = len(array)
        if length == 0:
            return []
        even = [] # 偶数
        odd = [] # 奇数
        for i in range(length):
            if array[i]%2 == 0:
                even.append(array[i])
            if array[i]%2 == 1:
                odd.append(array[i])
        return odd + even
