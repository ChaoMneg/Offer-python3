# -*- coding:utf-8 -*-
"""
题目：字符串的排列
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

思路：
1、求第一个位置的字符
2、固定第一个字符，求后边所有字符的排列
"""
class Solution:
    def Permutation(self, ss):
        if len(ss) <= 1:
            return ss
        res = set()
        # 遍历字符串，固定第一个元素，第一个元素可以取a,b,c...，然后递归求解
        for i in range(len(ss)):
            # 依次固定了元素，其他的全排列（递归求解）
            for j in self.Permutation(ss[:i] + ss[i+1:]): 
                # 集合添加元素的方法add(),集合添加去重（若存在重复字符，排列后会存在相同，如baa,baa）
                res.add(ss[i] + j) 
        return sorted(res) # sorted()能对可迭代对象进行排序,结果返回一个新的list
