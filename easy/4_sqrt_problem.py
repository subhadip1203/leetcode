'''
link: https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and return the square root of x.
'''

import math 
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))

print(Solution().mySqrt(4))
print(Solution().mySqrt(8))
print(Solution().mySqrt(9))