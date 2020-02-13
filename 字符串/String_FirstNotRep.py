# -*- coding:utf-8 -*-
"""
题目：第一个只出现一次的字符
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

思路：
1、字典存储遍历到的字符，遍历到一次+1

"""
class Solution:
    def FirstNotRepeatingChar(self, s):
        hash_map = {} # 存储字符次数
        if s == "":
            return -1
        for i in s:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        for j in s:
            if hash_map[j] == 1:
                return s.index(j) # 返回字符位置
                
            
