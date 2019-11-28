# -*- coding: utf-8 -*-
# @Time    : 2019-11-28 13:16
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_917_Reverse_Only_Letters.py
# @Software: PyCharm

'''
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.




'''


# class Solution(object):
    # def reverseOnlyLetters(self, S):#function
    #     """
    #     :type S: str
    #     :rtype: str
    #     """
    #     dicts,listsparams,strparams={},[],""
    #     lens=len(S)
    #     for element in range(lens):
    #         if not "a" <= S[element] <="z" and  not  "A" <=  S[element]<= "Z":
    #             dicts[element]=S[element]
    #         else:
    #             listsparams.append(S[element])
    #     listsparams=listsparams[::-1]
    #     for key in dicts.keys():
    #         listsparams.insert(key,dicts[key])
    #     return ''.join(listsparams)
    #







if __name__ == '__main__':
    s=Solution()
    seq="a-bC-dEf-ghIj"
    print(s.reverseOnlyLetters(seq))