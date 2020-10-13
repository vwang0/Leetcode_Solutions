"""
0064. Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        for i in range(1,col):
            grid[0][i] += grid[0][i-1]
        for j in range(1, row):
            grid[j][0] += grid[j-1][0]
        for k in range(1, row):
            for l in range(1, col):
                grid[k][l] += min(grid[k-1][l], grid[k][l-1])
        return grid[-1][-1]