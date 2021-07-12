'''
Link : https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
'''

class Solution:
    def canBeIncreasing(self, nums) :
        remove_num = 0
        nums = [0] + nums + [1001]
        for i in range(len(nums) - 3):
            if nums[i + 1] >= nums[i + 2]:
                if remove_num:
                    return False
                if nums[i] >= nums[i + 2] and nums[i + 1] >= nums[i + 3]:
                    return False
                remove_num = 1
        return True
            


nums = [1,2,10,5,7]
print(Solution().canBeIncreasing(nums))

nums = [1,2,5,7]
print(Solution().canBeIncreasing(nums))

nums = [2,3,1,2]
print(Solution().canBeIncreasing(nums))

nums = [1,1,1]
print(Solution().canBeIncreasing(nums))

nums = [1,2,3]
print(Solution().canBeIncreasing(nums))