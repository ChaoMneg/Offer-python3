# -*- coding: utf-8 -*-
# @Time    : 2020/2/2/002 10:26
# @Author  : mengchao
# @Site    : 
# @File    : String_R_Null.py
# @Software: PyCharm
"""
题目：替换空格
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

"""
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        r_result = s.replace(" ", "%20")
        return r_result
