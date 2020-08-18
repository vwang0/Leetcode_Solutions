"""
0994. Rotting Oranges
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) :
        m,n=len(grid),len(grid[0])
        count1=sum(1 if grid[i][j]==1 else 0 for i in range(m) for j in range(n))
        q=collections.deque([(i,j,0) for i in range(m) for j in range(n) if grid[i][j]==2])#add all 2 in queue
        time=0
        while q:
            x,y,time=q.popleft()
            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                r,c=x+i,y+j
                if 0<=r<m and 0<=c<n and grid[r][c]==1:
                    grid[r][c]=2
                    q.append((r,c,time+1))
                    count1-=1
        return time if count1==0 else -1        

