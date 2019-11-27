# -*- coding: utf-8 -*-
# @Time    : 2019-11-27 11:53
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_557.py
# @Software: PyCharm

'''

557. Reverse Words in a String III

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''


class Solution():
    def reverseWords(self, s: str) -> str:
        strtmp=''
        for element in s.split(" "):
            if element!=None:
                strtmp+=element[::-1]
                strtmp+=" "
            else:
                pass
        return strtmp.strip()
if __name__ == '__main__':
    s=Solution()
    seq="Let's take LeetCode contest"
    print (s.reverseWords(seq))
