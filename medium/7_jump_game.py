'''
https://leetcode.com/problems/jump-game/

solution : https://www.youtube.com/watch?v=muDPTDrpS28&t=610s
'''

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachableIndex = 0
        list_length = len(nums)
        for i in range(list_length):
            if i + nums[i] > maxReachableIndex:
                maxReachableIndex = i + nums[i]
                # print(maxReachableIndex)
                if maxReachableIndex > list_length-1:
                    return True
        return False


nums = [2, 3, 1, 1, 4]
print(Solution().canJump(nums))
