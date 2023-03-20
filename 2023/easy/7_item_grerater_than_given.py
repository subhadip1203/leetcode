
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

'''
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. 
There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. 
If such a character does not exist, return the first character in letters.


my first thought:
    1. i will loop through the arry
    2.  what ever will be larger than the item , will return that
'''

def nextGreatestLetter(letters, target):
    result = None
    for x in letters:
        if x > target and result == None:
            result = x
        elif x > target and x < result:
            result = letters[x]

    if result == None:
        return letters[0]
    else:
        return result

letters = ["c","f","j"]
target = "a"
print(nextGreatestLetter(letters, target))


letters = ["c","f","j"]
target = "c"
print(nextGreatestLetter(letters, target))


letters = ["x","x","y","y"]
target = "z"
print(nextGreatestLetter(letters, target))