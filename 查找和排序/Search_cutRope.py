# -*- coding:utf-8 -*-
"""
题目：剪绳子
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。
请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""
class Solution:
    # number：绳子长度
    def cutRope(self, number):
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        if number == 4:
            return 4
        # n >=5时，3(n-3) > 2(n-2)，尽量剪长度为3的绳子
        count_three  = number // 3 # 3的个数
        count_two = number % 3 # 2的个数
        if count_two == 1:
            return 3 ** count_three * 4 # 3^(count_three) * 4
        elif count_two == 0:
            return 3 ** count_three
        else:
            return 3 ** count_three * 2
