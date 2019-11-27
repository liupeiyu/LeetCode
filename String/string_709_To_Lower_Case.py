#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019-11-26 22:37 
# @name: string_709
# @author：peiyu
'''
709. To Lower Case

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.



Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
'''


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()

if __name__ == '__main__':

    s=Solution()
    seq="LOVELY"
    print(s.toLowerCase(seq))

