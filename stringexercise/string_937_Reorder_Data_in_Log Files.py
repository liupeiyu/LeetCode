# -*- coding: utf-8 -*-
# @Time    : 2019-12-03 20:18
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_937_Reorder_Data_in_Log Files.py
# @Software: PyCharm

'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.



Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]


'''


class Solution(object):
    def reorderLogFiles(self, logs):
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key = lambda x: (' '.join(x.split()[1:]), x.split()[0]) )
        return letters + digits


if __name__ == '__main__':
    s=Solution()
    slist=["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print(s.reorderLogFiles(slist))