
# https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



''' 
my thoughts 1:  convert array into dictonary  
    Time complexicity : N
    spacpe complexity: N

'''

def findDuplicate(arr):
    if len(arr) == 1 or len(arr) == 0:
        return True
    else:
        myDict = {}
        for x in arr:
            if x in myDict:
                return True
            else:
                myDict[x] = 1

        return False

nums = [1,2,3,1]
print(findDuplicate(nums))
nums = [1,2,3,4]
print(findDuplicate(nums))
nums = [1,1,1,3,3,4,3,2,4,2]
print(findDuplicate(nums))
