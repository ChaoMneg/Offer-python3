# -*- coding:utf-8 -*-
"""
题目：把数组排成最小的数
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

思路：
1、将数字转换为字符
2、判断x+y 与 y+x的大小，按判断的值将数组按从小到大排序
3、拼接字符
"""
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
        num = map(str, numbers) # 将数字转为字符
        # lambda：x,y--输入参数， cmp()---调用的函数
        num.sort(lambda x,y: cmp(x+y, y+x)) # 对比x+y与y+x，并排序(python3取消了cmp()函数)
        return "".join(num) # 使用""链接num
