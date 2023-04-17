
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/




'''
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Input: nums = [1,1]
Output: [2]

my thoughts :
    1. get length of array
    2. make dict of those mumbers as key like { 1: false , 2: false , 3 : false}
    3. loop through the array , and make those items as true
    4. return those item that are not true
'''

def findMissing(nums):
    result= []
   
    for item in nums:
        index = abs(item)-1
        nums[index]= -1 * abs(nums[index])
        

    for index , item in enumerate(nums):
        if item > 0 :
            result.append(index+1)
    
    return result



# youtube solution : https://www.youtube.com/watch?v=8i-f24YFWC4

# 1. find each item by loop
# 2.  change the item into index . like index  = item -1  ( but ite may be negative , so do index  = abs(item) -1  )
# 3. after geting the index , change in value of that index into negative (but the value may be already negative)
#       so do arr[index] = -1 * abosoluteValue( arr[index]  )
# 4. again , loop through the arr with index and value
# 5. return those index where value is not negative



nums = [4,3,2,7,8,2,3,1]
print(findMissing(nums))