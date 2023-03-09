# https://leetcode.com/problems/single-number/

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

def findNum(arr):
    result = 0
    for x in arr:
        result ^= x
    return result

nums = [2,2,1]
print(findNum(nums))

nums = [4,1,2,1,2]
print(findNum(nums))