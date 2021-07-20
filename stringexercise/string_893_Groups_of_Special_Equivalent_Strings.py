# -*- coding: utf-8 -*-
# @Time    : 2019-11-26 20:00
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_893.py
# @Software: PyCharm

'''



'''
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        B = set()
        for a in A:
            B.add(''.join(sorted(a[0::2])) + ''.join(sorted(a[1::2])))
        return len(B)

if __name__ == '__main__':
    A = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
    s = Solution()
    print("result : "+str(s.numSpecialEquivGroups(A)))