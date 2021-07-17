"""
link : https://leetcode.com/problems/find-the-town-judge/
"""

class Solution:
    def findJudge(self, n, trust) :
        if len(trust) < n-1 : # insufficient edge
            return -1
        degree=[0]*(n+1)
        for from_val, to_val in trust:
            degree[from_val] -= 1
            degree[to_val] += 1

        for i in range(1,n+1):   
            if degree[i]== n-1:
                return i          
        return -1


n = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
print(Solution().findJudge(n,trust))

n = 3
trust = [[1,2],[2,3]]
print(Solution().findJudge(n,trust))


n = 3
trust = [[1,3],[2,3],[3,1]]
print(Solution().findJudge(n,trust))

n = 2
trust = [[1,2]]
print(Solution().findJudge(n,trust))