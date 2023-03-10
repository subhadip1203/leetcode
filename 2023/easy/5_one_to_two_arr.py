# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/


'''
You are given a 0-indexed 1-dimensional (1D) integer array original, 
and two integers, m and n. You are tasked with creating a 2-dimensional (2D) 
array with  m rows and n columns using all the elements from original.
'''

def construct2DArray(original,m,n):
    ans = []
    if len(original) == m*n: 
        for i in range(0, len(original), n): 
            ans.append(original[i:i+n])
    return ans

original = [1,2,3,4,5,6,7,8,9,10]
m = 2
n = 5
print(construct2DArray(original,m,n))

original = [1,2,3]
m = 1
n = 3
print(construct2DArray(original,m,n))