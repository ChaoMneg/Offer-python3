# -*- coding: utf-8 -*-
# @Time    : 2020/2/2/002 10:44
# @Author  : mengchao
# @Site    : 
# @File    : String_regular_expression.py
# @Software: PyCharm

"""
题目：正则表达匹配
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

解题：
使用字符串匹配正则式，例如aaa去匹配“a.a”和“ab*ac*a”

特殊情况
1、两个字符串均为空，返回True
2、第一个字符串非空，第二个为空，返回false
（第一个空，第二个非空可能匹配成功，因为“*”可以表示0次，例如第二个字符串是“a*a*a*a*”,有可能匹配成功）

一般情况
1、pattern中第二个字符是"*"
如果s与pattern中第一个字符匹配
三种情况:
    s不变，pattern后移2个，相当于把pattern前两位当成空，匹配后面的
    s后移1个，pattern后移2个，相当于pattern前两位与s[0]匹配
    s后移1个，pattern不变，相当于pattern前两位，与s中的多位进行匹配，因为*可以匹配多位

如果s与pattern中第一个字符不匹配：s保持不变，pattern跳过* 匹配后边字符

2、假设pattern中第二个字符不是"*"
    判定s是否为空，空-false
    s 与 pattern第一个字符匹配，或者pattern第一个字符='.'---跳过第一个字符进行匹配

"""
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        l_s = len(s)
        l_pattern = len(pattern)
        # 两种特殊情况
        # 如果s与pattern都为空，则True
        if l_s == 0 and l_pattern == 0:
            return True
        # 如果s不为空，而pattern为空，则False
        if l_s != 0  and l_pattern == 0:
            return False

        # 一般情况
        # pattern中第二个字符是 *
        if l_pattern > 1 and pattern[1] == '*':
            # s 与 pattern第一个字符匹配
            if l_s != 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)

            # 三种情况:
            # s不变，pattern后移2个，相当于把pattern前两位当成空，匹配后面的
            # s后移1个，pattern后移2个，相当于pattern前两位与s[0]匹配
            # s后移1个，pattern不变，相当于pattern前两位，与s中的多位进行匹配，因为*可以匹配多位
            else:
                # s 与 pattern第一个字符不匹配，s保持不变，pattern跳过* 匹配后边字符
                return self.match(s, pattern[2:])


        # 假设pattern中第二个字符不是 *，跳过第一个直接匹配字符，匹配不到false
        if l_s > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        return False


s = Solution()
r = s.match("bcbbabab",".*a*a")
print(r)


