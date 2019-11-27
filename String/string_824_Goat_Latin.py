# -*- coding: utf-8 -*-
# @Time    : 2019-11-27 14:50
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_824_Goat_Latin.py
# @Software: PyCharm

'''
824. Goat Latin


A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.



Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


'''


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        rstr=''
        count=1
        slist=["a","e","i","o","u","A","E","I","O","U"]
        for seq in S.split(" "):
            if seq[0] in slist:
                rstr+=seq+"ma"+"a"*count+" "
            else:
                rstr+=seq[1:]+seq[0]+"ma"+"a"*count+" "
            count+=1
        return rstr.strip()





if __name__ == '__main__':

    s=Solution()
    seq="I speak Goat Latin"
    print(s.toGoatLatin(seq))
