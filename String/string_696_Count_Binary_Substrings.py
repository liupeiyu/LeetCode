# -*- coding: utf-8 -*-
# @Time    : 2019-12-02 16:41
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_696_Count_Binary_Substrings.py
# @Software: PyCharm

'''

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.


'''


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        res = 0
        for i in range(N):
            c1, c0 = 0, 0
            if s[i] == "1":
                c1 = 1
            else:
                c0 = 1
            for j in range(i + 1, N):
                if s[j] == "1":
                    c1 += 1
                else:
                    c0 += 1
                if c0 == c1:
                    res += 1
                    break
        return res





if __name__ == '__main__':
    s=Solution()
    seq='00110011'
    print(s.countBinarySubstrings(seq))