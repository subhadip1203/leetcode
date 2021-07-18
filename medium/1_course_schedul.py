"""
Link : https://leetcode.com/problems/course-schedule/
video : https://www.youtube.com/watch?v=EgI5nU9etnU&t=371s

learn : cycle detection algorithm
"""

class Solution:
    def canFinish(self, numCourses, prerequisites) :
        initial_dict = {i:[] for i in range(numCourses)}
        
        for crs , pre in prerequisites :
            initial_dict[crs].append(pre)

        visitedSet = set()
        def dfs(crs):
            if crs in visitedSet :
                return False
            if initial_dict[crs] == []:
                return True
            visitedSet.add(crs)
            for pre in initial_dict[crs]:
                if dfs(pre) == False:
                    return False
            visitedSet.remove(crs) 
            initial_dict[crs]=[]      
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True


numCourses = 2
prerequisites = [[1,0],[0,1]]
print(Solution().canFinish(numCourses,prerequisites))

numCourses = 2
prerequisites = [[1,0]]
print(Solution().canFinish(numCourses,prerequisites))
