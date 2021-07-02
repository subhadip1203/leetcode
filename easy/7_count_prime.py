'''
Link : https://leetcode.com/problems/count-primes/
Count the number of prime numbers less than a non-negative number, n.
'''

class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        dp = [True] * n
        dp[0] = dp[1] = False
        for i in range(2, n):
            if dp[i]:
                for j in range(i*i, n, i):
                    dp[j] = False
        return sum(dp)

n=10
print(Solution().countPrimes(n))

n=0
print(Solution().countPrimes(n))

n=1
print(Solution().countPrimes(n))

n=5
print(Solution().countPrimes(n))