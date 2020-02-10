# -*- coding:utf-8 -*-
"""
题目：包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

思路：
利用一个辅助栈来存放最小值，每入栈一次，就与辅助栈顶比较大小，如果小就入栈，如果大就入栈当前的辅助栈顶，当出栈时，辅助栈也要出栈
栈  3，4，2，5，1
辅助栈 3，3，2，2，1
"""
class Solution:
    def  __init__(self):
        self.stack = [] # 数据栈
        self.minStock = [] # 辅助栈
    def push(self, node):
        min = self.min()
        # 排除非数字
        if not min or node < min:
            self.minStock.append(node)
        else:
            self.minStock.append(min)
        self.stack.append(node)
    
    # 弹出数据
    def pop(self):
        if self.stack:
            self.minStock.pop()
            self.stack.pop()
    # 返回数据栈顶部数据
    def top(self):
        if self.stack:
            return self.stack[-1]
    # 返回辅助栈顶部数据
    def min(self):
        if self.minStock:
            return self.minStock[-1]
