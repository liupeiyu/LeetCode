# -*- coding: utf-8 -*-
# @Time    : 2019-12-13 20:09
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_1071_Greatest_Common_Divisor_of_Strings.py
# @Software: PyCharm

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1.__eq__(str2):
            return str1
        if len(str1)>len(str2):
            pass
