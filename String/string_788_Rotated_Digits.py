# -*- coding: utf-8 -*-
# @Time    : 2019-11-28 15:46
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_788_Rotated_Digits.py
# @Software: PyCharm

'''

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

'''


# class Solution(object):
#     def rotatedDigits(self, N):
#         """
#         :type N: int
#         :rtype: int
#         """
#


# zip('ABCD', 'xy') --> Ax By
