"""
695. Max Area of Island
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
# BFS Solution
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]):
        n, m = len(grid), len(grid[0])
        def bfs(i, j):
            q = deque([(i, j)])
            grid[i][j] = 0
            res = 0
            while len(q)>0:
                for i in range(len(q)):
                    (x, y) = q.popleft()
                    res += 1
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        x2, y2 = x+dx, y+dy
                        if 0<=x2<n and 0<=y2<m and grid[x2][y2]:
                            grid[x2][y2] = 0
                            q.append((x2, y2))
            return res

        area = [bfs(i, j) for i in range(n) for j in range(m) if grid[i][j]]
        return max(area) if area else 0

# DFS solution
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]):
        n, m = len(grid), len(grid[0])
        def dfs(i, j):
            if 0<=i<n and 0<=j<m and grid[i][j]:
                # mark as visited
                grid[i][j] = 0
                return 1+dfs(i+1, j)+dfs(i-1, j)+dfs(i, j+1)+dfs(i, j-1)
            return 0

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res        