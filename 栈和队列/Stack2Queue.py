# -*- coding: utf-8 -*-
# @Time    : 2020/2/6/006 16:19
# @Author  : mengchao
# @Site    : 
# @File    : Stack2Queue.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # stack1 插入数据
    def push(self, node):
        self.stack1.append(node)

    # stack1弹出数据后，stack2入栈将数据翻转
    def pop(self):
        if self.stack2 == []:
            while self.stack1:
                tmpNode = self.stack1.pop()
                self.stack2.append(tmpNode)
        return self.stack2.pop()
