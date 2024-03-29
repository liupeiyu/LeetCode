
#encoding:utf-8
'''
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

'''

class Solution:
    def findRepeatNumber(self, nums:[list]) -> list:
        di={}
        result=[]
        for i in nums:
            if i not in di.keys():
                di[i]=1
            else:
                di[i]+=1
        for i in di.keys():
            if di[i]>=2:
                result.append(i)

        return result

if __name__ == '__main__':

    b = Solution()
    nums=[2,3,4,5,4,3]
    print(b.findRepeatNumber(nums))
