# -*- coding:utf-8 -*-
"""
题目：扑克牌顺子
一副牌，大\小王（0）可以看成任何数字,并且A看作1,J为11,Q为12,K为13
现在,要求你使用这幅牌模拟输入的5张牌是不是顺子

思路：
1、如果输入为空，返回false
2、排序，统计王(0)的数量
3、计算(i+1) - i, 如果后面一个数比前面一个数大于1以上，那么中间的差值就必须用王来补了
"""
class Solution:
    def IsContinuous(self, numbers):
        # 如果numbers为空，false
        if not numbers:
            return False
        numbers.sort() # 排序
        zeorNum = numbers.count(0) # 统计0的数量
        # enumerate()将字符串组合为一个索引序列，同时列出数据和数据下标
        # numbers[:-1] ：所有字符
        for i, value in enumerate(numbers[:-1]):
            if value != 0:
                if numbers[i+1] == value:
                    return False
                # 如果后面一个数比前面一个数大于1以上, 使用王来补齐(+ 1可抵消相差的1)
                zeorNum = zeorNum - (numbers[i+1] - value) + 1
                if zeorNum < 0:
                    return False
        return True
