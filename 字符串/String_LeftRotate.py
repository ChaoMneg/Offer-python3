# -*- coding:utf-8 -*-
"""
题目：左旋转字符串
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！

思路：
1、将字符串分为两部分
2、分别翻转两部分字符
3、翻转全部字符
"""
class Solution:
    def LeftRotateString(self, s, n):
        if s != None:
            length = len(s)
            res = [] 
            # 将字符存储到list，方便赋值操作
            for i in range(length):
                res.append(s[i])
            # 字符翻转
            if length > 0  and n >0 and n < length:
                # 翻转第一部分
                self.Reverse(0, n-1, res)
                # 翻转第二部分
                self.Reverse(n, length-1, res)
                # 全部翻转
                self.Reverse(0, length-1, res)
            return "".join(res)
    # 字符翻转函数
    def Reverse(self, begin, end, s):
        if begin == None or end == None:
            return ""
        while begin < end:
            s[begin],s[end] = s[end],s[begin]
            begin = begin + 1
            end = end - 1
            
