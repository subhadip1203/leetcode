'''
Link : https://leetcode.com/problems/minimum-height-trees/
'''

class Solution:
    def findMinHeightTrees(self, n, edges) :
        if n <= 2:
            return [x for x in range(n)]
        else:
            my_list=[]
            return my_list