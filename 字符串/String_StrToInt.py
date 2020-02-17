# -*- coding:utf-8 -*-
"""
题目：把字符串转换成整数
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0

备注：
python2测试，需要边界判断
"""
class Solution:
    def StrToInt(self, s):
        numList = ['0','1','2','3','4','5','6','7','8','9']
        intNum = 0
        label = 1 # 正负标志位
        if s == "":
            return 0
        # 判断首位
        if s[0] == "+":
            label = 1
            s = s[1:]
        elif s[0] == "-":
            label = -1
            s = s[1:]
        else:
            pass # 占位符
        for i in s:
            if i in numList:
                intNum = intNum*10 + numList.index(i)
            if i not in numList:
                intNum = 0
                break
            # 边界判断
            if label == 1 and intNum > 0x7FFFFFFF:
                intNum = 0
                break
            if label == -1 and intNum > 0x80000000:
                intNum = 0
                break
        return intNum*label
