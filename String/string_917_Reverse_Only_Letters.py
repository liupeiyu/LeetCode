# -*- coding: utf-8 -*-
# @Time    : 2019-11-28 13:16
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_917_Reverse_Only_Letters.py
# @Software: PyCharm

'''
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.




'''


class Solution(object):
    def reverseOnlyLetters(self, S):#function
        """
        :type S: str
        :rtype: str
        """
        dicts,listsparams,strparams={},[],""
        lens=len(S)
        for element in range(lens):
            if not "a" <= S[element] <="z" and  not  "A" <=  S[element]<= "Z":
                dicts[element]=S[element]
            else:
                listsparams.append(S[element])
        listsparams=listsparams[::-1]
        for key in dicts.keys():
            listsparams.insert(key,dicts[key])
        return ''.join(listsparams)
    #


# class Solution:
#     def reverseOnlyLetters(self, S: str) -> str:
#         str_list = []
#         not_letter_dict = {}
#         for i, j in enumerate(S):
#             if j.isalpha():
#                 str_list.append(j)
#             else:
#                 not_letter_dict[i] = j
#
#         reversed_list = str_list[::-1]
#
#         for i in not_letter_dict.keys():
#             reversed_list.insert(i, not_letter_dict[i])
#         return ''.join(reversed_list)




if __name__ == '__main__':
    s=Solution()
    seq="a-bC-dEf-ghIj"
    print(s.reverseOnlyLetters(seq))