# -*- coding: utf-8 -*-
# @Time    : 2020/1/31/031 15:54
# @Author  : mengchao
# @Site    : 
# @File    : Array_duplicate_numbers.py
# @Software: PyCharm

"""
题目: 数组中重复的数字
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
"""

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False

    # 修改数组
    def duplicate(self, numbers, duplication):
        n = len(numbers)
        for i in range(n):
            if numbers[i] != i:
                tmp = numbers[numbers[i]]
                if tmp == numbers[i]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    numbers[numbers[i]] = numbers[i]
                    numbers[i] = tmp
        return False


    # 不修改数组，P43
    def duplicate_2(self, numbers, duplication):
        n = len(numbers)
        start = 1
        end = n

        while end >= start:
            middle = ((end - start) >> 1) + start
            count_n = count(numbers, n, start, middle)
            if start == end:
                if count_n > 1:
                    return start
                else:
                    break
            elif count_n > (middle - start +1):
                end = middle
            else:
                start = middle + 1
        return -1


# 计数函数，算法2使用
def count(numbers, len, start, end):
    count_n = 0
    for i in range(len):
        if numbers[i] >= start and numbers[i] <= end:
            count_n = count_n + 1
    return count_n


# 测试用例 [2,3,1,0,2,5,3]
S = Solution()
duplication = ["a"]
numbers = [2,3,1,0,2,5,3]
d_result = S.duplicate_2(numbers, duplication)
print(d_result)
