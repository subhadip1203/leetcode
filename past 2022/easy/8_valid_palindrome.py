'''
Link : https://leetcode.com/problems/valid-palindrome/
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''

class Solution:
    def isPalindrome(self, s: str) -> str:
        s=s.lower()
        i=0
        j= len(s)-1
        while i<= j :
            while s[i].isalnum() == False:
                i+=1
            while s[j].isalnum() == False:
                j-=1
            if s[i] != s[j] :
                return False
            else:
                i+=1
                j-=1

        return True

s = "A man"
print(Solution().isPalindrome(s))

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))

s = "race a car"
print(Solution().isPalindrome(s))