'''
Link : https://leetcode.com/problems/number-of-provinces/

solution : https://www.youtube.com/watch?v=S5UUvCTM0V4
'''


from typing import List


def findCircleNum(self, isConnected: List[List[int]]) -> int:
    length = len(isConnected)
    visited = [0]*length

    def dfs(node):
        visited[node] = True
        for j in range(0, length):
            if isConnected[node][j] == 1 and visited[j] is False:
                dfs(j)

    count = 0

    for i in range(0, length):
        if visited[i] is False:
            count += 1
            dfs(i)
    return count
