# -*- coding: utf-8 -*-
# @Time    : 2019-11-28 10:33
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_max_character.py
# @Software: PyCharm


class Solutions(object):
    def maxFrequencyInList(self,s):

        '''
        :param s:list
        :return:
        '''
        dicts_s,list_s={},[]
        for element in s:
            if element not in dicts_s:
                dicts_s[element]=1
            else:
                dicts_s[element]+=1

        for key in dicts_s.keys():
            list_s.append(dicts_s[key])



        return max(list_s)

    def minFrequencyInSList(self,s):
        dicts_s,list_s={},[]
        for element in s:
            if element not in dicts_s:
                dicts_s[element]=1
            else:
                dicts_s[element]+=1

        for key in dicts_s.keys():
            list_s.append(dicts_s[key])
        return min(list_s)

    def MaxFrequencyInString(self,s):
        '''

        :param s:  str
        :return:
        '''
        str_params= " ".join(s)
        li=str_params.split(" ")
        return  self.maxFrequencyInList(li)

    def MinFrequencyInString(self,s:str):
        '''

        :param s: str
        :return:
        '''
        elementlist=[]
        for element in set(s):
            elementlist.append(s.count(element))
        return min(elementlist)

if __name__ == '__main__':

    s=Solutions()
    listParams="aabbccddddd"
    print(s.MinFrequencyInString(listParams))