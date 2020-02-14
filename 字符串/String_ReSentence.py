# -*- coding:utf-8 -*-
"""
题目：翻转单词顺序列
将“I am a student.”翻转为“student. a am I”
"""
class Solution:
    def ReverseSentence(self, s):
        return " ".join(s.split(" ")[::-1])
        
