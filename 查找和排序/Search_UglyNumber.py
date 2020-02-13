# -*- coding:utf-8 -*-
"""
题目：丑数
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

思路：
1、将第一个丑数存到一个List
2、设立三个指针，分别表示2，3，5的位置
3、第一个丑数*（2,3,5） 区最小的一个放到第一个丑数后边，循环
"""
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0
        uglyList = [1] # 丑数
        # 2,3,5对应的指针
        twoPointer = 0
        threePointer = 0
        fivePointer = 0
        
        count = 1
        while count != index:
            # List里第一个值分别乘 2， 3， 5
            minValue = min(2*uglyList[twoPointer], 3*uglyList[threePointer], 5*uglyList[fivePointer])
            uglyList.append(minValue)
            count += 1
            
            # 移动三个指针
            if minValue == 2*uglyList[twoPointer]:
                twoPointer += 1
            if minValue == 3*uglyList[threePointer]:
                threePointer += 1
            if minValue ==  5*uglyList[fivePointer]:
                fivePointer += 1
        return uglyList[count-1]
