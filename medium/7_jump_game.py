'''
https://leetcode.com/problems/jump-game/
'''

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lastpos = n-1
        for i in range(n-1, -1, -1):
            if i + nums[i] >= lastpos:
                lastpos = i

        return lastpos == 0


nums = [2, 3, 1, 1, 4]
print(Solution().canJump(nums))
