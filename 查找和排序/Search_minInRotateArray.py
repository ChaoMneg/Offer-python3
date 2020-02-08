# -*- coding: utf-8 -*-
# @Time    : 2020/2/8/008 10:36
# @Author  : mengchao
# @Site    : 
# @File    : Search_minInRotateArray.py
# @Software: PyCharm

"""
题目：旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
# 使用二分查找
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        length = len(rotateArray)
        if length == 0:
            return 0

        left = 0   # 开始索引
        right = length - 1  # 结尾索引
        mid = left  # 中间值索引

        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                mid = right
                break

            mid = (left + right) / 2  # 获取中间值索引
            # 如果中间值>开始值，则中间值属于第一部分，继续遍历右半部分
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            # 如果中间值<开始值, 则中间值属于第二部分，继续遍历左半部分
            elif rotateArray[mid] <= rotateArray[right]:
                right = mid
        return rotateArray[mid]
