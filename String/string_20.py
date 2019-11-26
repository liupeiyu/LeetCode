#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019-11-25 23:20 
# @name: string_20
# @author：peiyu

'''

Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.


'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        number_a,number_b,number_c=0,0,0
        for i in s:
            if i=="(":
                number_a+=1
            if i==")":
                number_a-=1
            if i=="{":
                number_b+=1
            if i=="}":
                number_b-=1
            if i=="[":
                number_c+=1
            if i=="]":
                number_c-=1
            if number_a<0 or number_b<0 or number_c<0:
                return "false"
        if number_c==0 and number_b==0 and number_a==0:
            return "true"
        else:
            return "false"


if __name__ == '__main__':
    s=Solution()
    strings="(]"
    print(s.isValid(strings))
