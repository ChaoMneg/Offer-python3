# -*- coding: utf-8 -*-
# @Time    : 2020/2/2/002 15:23
# @Author  : mengchao
# @Site    : 
# @File    : String_isNumeric.py
# @Software: PyCharm

# -*- coding:utf-8 -*-
"""
题目：表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""

import re
class Solution:

    # s字符串
    """
    ^ : 开头
    [\+\-]? ：正或负符号出现与否
    [0-9]* ：匹配0个或0个以上的0-9之间的数字
    (\.[0-9])? ：小数点后边是否为0-9
    ([eE][\+\-]?[0-9]+)? ：[eE]出现后是否有+、-, 之后是否跟数字0-9
    $：结尾
    """
    # 正则表达式
    def isNumeric(self, s):
        if len(s) == 0:
            return False
        else:
            return re.match("^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$", s)

s =Solution()
a = s.isNumeric("123.45e+6")
print(a)
