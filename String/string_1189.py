#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019-11-22 22:33 
# @name: string_1189
# @author：peiyu

'''

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



'''

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count_b,count_a,count_o,count_l,count_n=0,0,0,0,0
        for  word in text:
            if word =='b':
                count_b+=1
            elif word=='a':
                count_a+=1
            elif word =='l':
                count_l+=1
            elif word == 'o':
                count_o+=1
            elif word =='n':
                count_n+=1
        if count_l<2 or count_o<2:
            return 0
        else:
            return min(count_n,count_o//2,count_l//2,count_a,count_b)





text="krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"


b=Solution()
print (b.maxNumberOfBalloons(text))