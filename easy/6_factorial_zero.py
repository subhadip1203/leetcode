'''
link: https://leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        i, total = 5, 0
        while i <= n:
            total += n // i
            i = i * 5
        return total

n=3
print(Solution().trailingZeroes(n))


n=5
print(Solution().trailingZeroes(n))


n=15
print(Solution().trailingZeroes(n))

n=0
print(Solution().trailingZeroes(n))

n=51
print(Solution().trailingZeroes(n))