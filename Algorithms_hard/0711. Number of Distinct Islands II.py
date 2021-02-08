"""
0711. Number of Distinct Islands II
Hard

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if they have the same shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or up/down direction).

Example 1:
11000
10000
00001
00011
Given the above grid map, return 1.

Notice that:
11
1
and
 1
11
are considered same island shapes. Because if we make a 180 degrees clockwise rotation on the first island, then two islands will have the same shapes.
Example 2:
11100
10001
01001
01110
Given the above grid map, return 2.

Here are the two distinct islands:
111
1
and
1
1

Notice that:
111
1
and
1
111
are considered same island shapes. Because if we flip the first array in the up/down direction, then they have the same shapes.
Note: The length of each dimension in the given grid does not exceed 50.
"""
class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            grid[x][y] = 0
            path.append((x, y))
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy]:
                    dfs(x + dx, y + dy)
        
        def normalize(path):
            return [(x - path[0][0], y - path[0][1]) for x, y in path]
        
        def rotate_valid(path):
            for i in range(3):
                path = normalize(sorted([(y, -x) for x, y in path]))
                if tuple(path) in res: return False
            return True
        
        def allvalid(path):
            if tuple(path) in res or not rotate_valid(path): return False
            hon_path = normalize(sorted([(-x, y) for x, y in path]))
            if tuple(hon_path) in res or not rotate_valid(hon_path): return False
            ver_path = normalize(sorted([(x, -y) for x, y in path]))
            if tuple(ver_path) in res or not rotate_valid(ver_path): return False
            return True
        
        res = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    path = []
                    dfs(i, j)
                    path = normalize(sorted(path))
                    if allvalid(path):
                        res.add(tuple(path))
        return len(res)