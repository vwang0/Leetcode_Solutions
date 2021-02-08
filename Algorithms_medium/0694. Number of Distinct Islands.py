"""
0694. Number of Distinct Islands
Medium

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        island_shapes = set()
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j, positions, rel_pos):
            grid[i][j] = -1
            for direction in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                next_i, next_j = i + direction[0], j + direction[1]
                if (0 <= next_i < rows and 0 <= next_j < cols) and grid[next_i][next_j] == 1:
                    new_rel_pos = (rel_pos[0] + direction[0], rel_pos[1] + direction[1])
                    positions.append(new_rel_pos)
                    dfs(next_i, next_j, positions, new_rel_pos)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    positions = []
                    dfs(i, j, positions, (0, 0))
                    island_shapes.add(tuple(positions))
        return len(island_shapes)