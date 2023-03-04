'''
Link : https://leetcode.com/problems/buddy-strings/

Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
'''

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) :
            return False
        if s == goal :
            return False if len(set(s))==len(s) else True
        diff =[]
        for i in range(len(s)):
            if s[i] != goal[i] :
                diff.append(i)
                if len(diff) > 2 :
                    return False
        if len(diff) != 2:
            return False
        else:
            return s[diff[0]]== goal[diff[1]] and s[diff[1]] == goal[diff[0]]

s = "ab"
goal = "ba"
print(Solution().buddyStrings(s,goal))

s = "accccb"
goal = "bccccca"
print(Solution().buddyStrings(s,goal))

s = "aa"
goal = "aa"
print(Solution().buddyStrings(s,goal))

s = "aaaaaaabc"
goal = "aaaaaaacb"
print(Solution().buddyStrings(s,goal))