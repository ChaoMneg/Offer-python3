# -*- coding:utf-8 -*-
"""
题目：求1+2+3+...+n
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""
class Solution:
    def Sum_Solution(self, n):
        sumN = n
        # 逻辑短路算法
        return (sumN and sumN + self.Sum_Solution(n-1))
