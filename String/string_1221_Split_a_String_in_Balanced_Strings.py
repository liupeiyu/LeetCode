#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019-11-26 22:29 
# @name: string_1221
# @author：peiyu

'''

1221. Split a String in Balanced Strings
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.



Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'



'''


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count,tmp=0,0
        for number in s:
            if number=="L":
                count+=1
            if number=="R":
                count-=1
            if count==0:
                tmp+=1
        return tmp


if __name__ == '__main__':
    s=Solution()
    seq="LLLLRRRR"
    print(s.balancedStringSplit(seq))