# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 3:21 下午
# @Author  : peiyu
# @FileName: number06.py
# @email   : lvegod@163.com
# @Blog    : https://github.com/liupeiyu/LeetCode
# class TreeNode:
'''
剑指 Offer 06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
'''
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        result=[]
        while head:
            result.append(head.val)
            head= head.next
        result.reverse()
        return result