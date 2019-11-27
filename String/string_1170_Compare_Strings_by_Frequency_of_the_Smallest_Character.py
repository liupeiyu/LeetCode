# -*- coding: utf-8 -*-
# @Time    : 2019-11-27 16:48
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_1170_Compare_Strings_by_Frequency_of_the_Smallest_Character.py
# @Software: PyCharm

'''
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.



Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").


'''

#function one
# class Solution(object):
#     def numSmallerByFrequency(self, queries, words):
#         """
#         :type queries: List[str]
#         :type words: List[str]
#         :rtype: List[int]
#         """
#         tmplist=[]
#         queries_number =self.getfrequencyNumber(queries)
#         words_number = self.getfrequencyNumber(words)
#         count=0
#         for i in queries_number:
#             for j in words_number:
#                 if i<j:
#                     count+=1
#                 else:
#                     pass
#             tmplist.append(count)
#             count=0
#         return tmplist
#     def getfrequencyNumber(self,slist):#获取列表中元素里面最小字符出现的频率
#         frequency,count=[],0
#         for element in slist:
#             for seq in element:
#                 if seq==min(element):
#                     count+=1
#             frequency.append(count)
#             count=0
#         return frequency


class Solution:
    def numSmallerByFrequency(self, queries, words):
        queries_frequecy = [self.f(i) for i in queries]
        words_frequecy = [self.f(i) for i in words]
        words_frequecy.sort()
        res = []
        length = len(words_frequecy)
        for i in range(len(queries_frequecy)):
            for j in range(length):
                if queries_frequecy[i] < words_frequecy[j]:
                    res.append(length - j)
                    break
            if len(res) < i + 1:
                res.append(0)
        return res

    def f(self, s):
        smallest = min(s)
        return s.count(smallest)

if __name__ == '__main__':
    s=Solution()
    qurieslist=["cbd"]
    wordslist=["zaaaz"]
    print(s.numSmallerByFrequency(qurieslist,wordslist))

