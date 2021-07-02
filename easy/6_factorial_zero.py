'''
link: https://leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        k, tot = 5, 0
        while k <= n:
            tot += n // k
            k = k * 5
        return tot

n=3
print(Solution().trailingZeroes(n))


n=5
print(Solution().trailingZeroes(n))


n=15
print(Solution().trailingZeroes(n))

n=0
print(Solution().trailingZeroes(n))