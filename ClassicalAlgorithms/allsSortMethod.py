# -*- coding: utf-8 -*-
# @Time    : 2019-11-28 10:33
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_max_character.py
# @Software: PyCharm

def select_sort_search():
    return

def binary_sort_search(li:list,val:int):
    left=0
    right=len(li)-1
    mid  = (left+right)//2
    while left<=right:
        if li[mid]==val:
            return mid
        elif li[mid]<val:
            left =mid+1
        else:
            right=mid-1
    return None