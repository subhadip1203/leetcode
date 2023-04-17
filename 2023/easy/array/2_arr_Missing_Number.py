
# https://leetcode.com/problems/missing-number/

'''
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.


my thoughts:
    1. save it in sorted array
    2. find the missing element by comparing i & i+1

after seeing solutions : better aproach :
    1. find max number and min num
    2. where n is the number of integers = in our case length of array
    3. sum should be  = (n / 2)(first number + last number) = sum,
    4. actualaddition - sum

'''


def calculation(nums):
    if len(nums) == 0:
        return 0

    minNum = nums[0]
    maxNum = nums[0]
    sum = 0

    for x in nums:
        if  minNum > x:
            minNum = x
        if maxNum < x:
            maxNum = x
        sum = sum+ x


    if minNum != 0:
        return 0  
 
    numberOfInt = (maxNum - minNum+1)
    idealSum = (numberOfInt/2)*(minNum+maxNum)

    if sum == idealSum :
        return int(maxNum+1)
    else:
        return int(idealSum - sum)

nums = [3,0,1]
print(calculation(nums))
nums = [0,1]
print(calculation(nums))
nums = [9,6,4,2,3,5,7,0,1]
print(calculation(nums))
nums = [1]
print(calculation(nums))
nums =[1,2]
print(calculation(nums))