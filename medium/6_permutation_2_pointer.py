'''
https://leetcode.com/problems/next-permutation/
'''
class Solution():
  def nextPermutation(self, nums):
    i, j = len(nums)-2, len(nums)-1

    # first largest number in the left side
    # and stop at smaller number
    while i >= 0 and nums[i+1] <= nums[i]:
      i -= 1 

    # finding smaller number than i
    if i >= 0: 
      while j >= 0 and nums[j] <= nums[i]: 
        j -= 1 # stop at larger number 
			# swap 
      nums[i], nums[j] = nums[j], nums[i]

		# reverse the number between two indexes 
    left, right = i+1, len(nums)-1
    while left < right:
      nums[left], nums[right] = nums[right], nums[left]
      left += 1
      right -= 1
    return nums

nums = [1,2,3]
print(Solution().nextPermutation(nums))
