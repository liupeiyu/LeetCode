# -*- coding: utf-8 -*-
# @Time    : 2019-11-25 16:47
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_14.py
# @Software: PyCharm

'''


编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。


'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        s1,s2= min(strs),max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

if __name__ == '__main__':

    s=Solution()

    listparams=["aca","cba"]
    print(s.longestCommonPrefix(listparams))









