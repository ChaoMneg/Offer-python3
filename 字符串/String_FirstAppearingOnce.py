# -*- coding: utf-8 -*-
# @Time    : 2020/2/2/002 16:37
# @Author  : mengchao
# @Site    : 
# @File    : String_FirstAppearingOnce.py
# @Software: PyCharm

"""
题目：字符流中第一个不重复的字符
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。
"""
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.hash_map = {}
    def FirstAppearingOnce(self):
        for i in self.s:
            if self.hash_map[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        self.s = self.s + char
        if char in self.hash_map:
            self.hash_map[char] = self.hash_map[char] + 1
        else:
            self.hash_map[char] = 1

