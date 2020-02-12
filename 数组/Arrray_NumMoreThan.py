# -*- coding:utf-8 -*-
"""
题目：数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

思路：
1、顺序遍历数组，将遍历到的值作为key存入字典
2、如果字典key中存在，该key对应的值+1； 如果不存在，则key对应值为1
"""
class Solution:
    # 时间复杂度未O(n), 空间复杂度为O(n)
    def MoreThanHalfNum_Solution(self, numbers):
        count = {} # 存放数值出现的次数
        length = len(numbers)
        for i in numbers:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            if count[i] > (length>>1):
                return i
        return 0
