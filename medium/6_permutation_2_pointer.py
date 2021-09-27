'''
https://leetcode.com/problems/next-permutation/
'''


class Solution():
    def nextPermutation(self, nums):
        left = len(nums)-2
        while left >= 0 and nums[left] >= nums[left+1]:
            left -= 1
        right = left+1
        while right < len(nums) and nums[right] > nums[left]:
            right += 1
        nums[left], nums[right-1] = nums[right-1], nums[left]
        nums[left+1:] = sorted(nums[left+1:])
        right -= 1
        return nums


nums = [1, 2, 3]
print(Solution().nextPermutation(nums))
