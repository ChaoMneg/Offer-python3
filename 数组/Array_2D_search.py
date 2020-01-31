# -*- coding: utf-8 -*-
# @Time    : 2020/1/31/031 13:32
# @Author  : mengchao
# @Site    : python 3.6
# @File    : Array_2D_search.py
# @Software: PyCharm


"""
题目：二维数组查找
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。

测试用例：7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
测试结果：牛客网测试通过 （牛客网同样的算法执行时间不同，不知道为什么，可能跟服务器的网络之类的有关吧)
"""

class Solution:
    # 方法1，直接查找
    def Find1(self, target, array):
        n = len(array)
        tag = "false"
        for i in range(n):
            if target in array[i]:
                tag = "true"
                break
        return tag

    # 方法2，剑指Offer解题算法
    def Find2(self, target, array):
        tag = "false"
        len_row = len(array)
        len_column = len(array[0])

        start_row = 0
        start_column = len_column - 1
        while start_row < len_row and start_column>=0:
            value = array[start_row][start_column]
            if (value > target):
                start_column = start_column - 1
            elif(value < target):
                start_row = start_row + 1
            else:
                tag = "true"
                break
        return tag

while True:
    try:
        S = Solution()
        l = list(eval(input()))
        target = l[0]
        array = l[1]
        f_result = S.Find2(target, array)
        print(f_result)
    except:
        break
