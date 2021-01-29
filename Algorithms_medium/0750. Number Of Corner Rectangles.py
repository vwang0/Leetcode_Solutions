"""
0750. Number Of Corner Rectangles
Medium

Given a grid where each entry is only 0 or 1, find the number of corner rectangles.

A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.

 

Example 1:

Input: grid = 
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
 

Example 2:

Input: grid = 
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
 

Example 3:

Input: grid = 
[[1, 1, 1, 1]]
Output: 0
Explanation: Rectangles must have four distinct corners.
 

Note:

The number of rows and columns of grid will each be in the range [1, 200].
Each grid[i][j] will be either 0 or 1.
The number of 1s in the grid will be at most 6000.
"""
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        dp_set = []
        res = 0
        for y in range(len(grid)):
            dp_set.append(set(idx for idx,val in enumerate(grid[y]) if val))
            for prev in range(y):
                matches = len(dp_set[y] & dp_set[prev])
                if matches >= 2:
                    res += matches * (matches-1) // 2            
        return res

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        h, w = len(grid), len(grid[0])
        res = 0
        for i in range(h -1):
            for j in range(i+1, h):
                count = 0
                for c in range(w):
                    if grid[i][c] and grid[j][c]:
                        res += count
                        count += 1
        return res


