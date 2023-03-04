'''
link : https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3812/

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the
'''

class Solution:
    def findPeakElement(self, nums):
        length = len(nums)        
        for i in range(length-2):
            if nums[i]<nums[i+1] and  nums[i+2] < nums[i+1]:
                return i+1
        # if only 2 elements are there or the first element is the largest element
        if length >1 and nums[0]> nums[1]: 
            return 0
        return length-1

nums = [1,2,3,1]
print(Solution().findPeakElement(nums))

nums = [1,2,1,3,5,6,4]
print(Solution().findPeakElement(nums))

nums=[2,1]
print(Solution().findPeakElement(nums))

nums=[1,2]
print(Solution().findPeakElement(nums))

nums=[3,2,1]
print(Solution().findPeakElement(nums))