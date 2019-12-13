# -*- coding: utf-8 -*-
# @Time    : 2019-12-10 12:10
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : Case_94_StringToInteger.py
# @Software: PyCharm
class Solution(object):
    def addStrings(self, num1, num2):
        num1, num2 = num1[::-1], num2[::-1]                     # 将输入字符串逆序
        len1, len2 = len(num1), len(num2)                       # 获得字符串长度
        res = ''                                                # 初始化结果变量
        carry = 0                                               # 初始化进位
        for i in range(max(len1, len2)):                        # 开始遍历
            n1 = ord(num1[i]) - ord('0') if i < len1 else 0     # 取第一个数的当前位
            n2 = ord(num2[i]) - ord('0') if i < len2 else 0     # 取第二个数的当前位
            s = n1 + n2 + carry                                 # 当前位的计算结果
            carry, r = s // 10, s % 10                          # 获得余数和进位
            res = str(r) + res                                  # 把余数加到当前结果的最高位
        if carry:                                               # 如果算完还有进位
            res = str(carry) + res                              # 加到结果最高位
        return res                                              # 返回最终结果

if __name__ == '__main__':
    s=Solution()
    lstring="9097798797896787687683648237648237648273648237487878"
    rstring="723482937492349273948723947239847923879823749273894872398472394723984792836487236487236488676"
    print(s.addStrings(lstring,rstring))