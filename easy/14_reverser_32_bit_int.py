class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        i = -rev if x < 0 else rev
        if i < -2**31 or i > 2**31-1:
            return 0
        return i

x = 123
print(Solution().reverse(x))

x = 120
print(Solution().reverse(x))

x = 0
print(Solution().reverse(x))

x = 3256789342456778
print(Solution().reverse(x))