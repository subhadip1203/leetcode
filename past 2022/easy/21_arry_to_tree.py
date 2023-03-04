"""
Link : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

video : https://www.youtube.com/watch?v=0K0uCMYq5ng
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        def helper(l,r):
            if(l>r):
                return None
            mid= (l+r)//2
            rootNode = TreeNode(nums[mid])
            rootNode.left = helper(l,mid-1)
            rootNode.right = helper(mid+1,r)
            return rootNode
        return helper(0,len(nums)-1)

nums = [1,3]
print(Solution().sortedArrayToBST(nums))
nums = [-10,-3,0,5,9]
print(Solution().sortedArrayToBST(nums))