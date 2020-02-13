# -*- coding:utf-8 -*-
"""
题目：数组中只出现一次的数字
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

思路1：使用字典，遍历到的值的次数存储到字典中

思路2：异或法

"""
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    # 思路1
    def FindNumsAppearOnce1(self, array):
        hashMap = {}
        res = []
        if array == None:
            return None
        for i in array:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        for j in hashMap:
            if hashMap[j] == 1:
                res.append(j)
        return res
   
    # 思路2:
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        
        # 所有数字进行异或操作
        tmp = 0
        for i in array:
            tmp ^= i
        # 获取tmp中最低位1的位置
        index = 0
        while tmp & 1 == 0:
            tmp >>= 1
            index += 1
        a = b = 0
        for j in array:
            if self.isBit(j, index):
                a ^= j
            else:
                b ^= j
        return [a, b]

    # index位是否为1
    def isBit(self, num, index):
        num = num >> index
        return num & 1
