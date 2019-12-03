#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019-12-01 10:59 
# @name: string_788_Rotated_Digits
# @author：peiyu

'''
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

'''

class Solution:
	def rotatedDigits(self, N: int) -> int:
		numb = set(['6','9','2','5', '1', '0', '8'])

		cnt = 0
		for i in range(1,N+1):
			t = set(str(i))
			if t-numb==set():
				if t-set(['8', '0', '1'])==set():
					pass
				else:
					cnt+=1
		return cnt

if __name__ == '__main__':
    s=Solution()

    print(s.rotatedDigits(10))