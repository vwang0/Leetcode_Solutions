"""
1778. Shortest Path in a Hidden Grid
Medium

This is an interactive problem.

You are given a robot in a hidden grid, and it wants to go to a target cell in this grid. The grid is of size m x n, and each cell in the grid can be empty or blocked. It is guaranteed that the start point and the robot's destination are different, and neither of them is blocked.

You want to find the robot's minimum distance to the target cell. However, you do not know the grid's dimensions, or the starting point of the robot, or its target destination. You are only allowed to ask queries to your GridMaster object.

You are given a class GridMaster which you can call the following functions from:

boolean GridMaster.canMove(char direction) returns true if the robot can move in that direction. Otherwise, it returns false.
void GridMaster.move(char direction) moves the robot in that direction. If this move would move the robot to a blocked cell or off the grid, it will be ignored, and the robot would remain in the same position.
boolean GridMaster.isTarget() returns true if the robot is currently on the target cell. Otherwise, it returns false.
Note that direction in the above functions should be a character from {'U','D','L','R'}, representing the directions up, down, left, and right, respectively.

Return the minimum distance between the robot's initial starting cell and the target cell if there is a path between them. Otherwise, return -1.

Custom testing:

The test input is read as a 2D matrix grid of size m x n where:

grid[i][j] == -1 indicates that the robot is in cell (i, j).
grid[i][j] == 0 indicates that the cell (i, j) is blocked.
grid[i][j] == 1 indicates that the cell (i, j) is empty.
grid[i][j] == 2 indicates that the cell (i, j) is the target cell.
There is exactly one -1 and 2 in grid. Remember that you will not have this information in your code.

 

Example 1:

Input: grid = [[1,2],[-1,0]]
Output: 2
Explanation: One possible interaction is described below:
The robot is initially standing on cell (1, 0), denoted by the -1.
- master.canMove('U') returns True.
- master.canMove('D') returns False.
- master.canMove('L') returns False.
- master.canMove('R') returns False.
- master.move('U') moves the robot to the cell (0, 0).
- master.isTarget() returns False.
- master.canMove('U') returns False.
- master.canMove('D') returns True.
- master.canMove('L') returns False.
- master.canMove('R') returns True.
- master.move('R') moves the robot to the cell (0, 1).
- master.isTarget() returns True. 
We now know that the target is the cell (0, 1), and the shortest path to the target is 2.
Example 2:

Input: grid = [[0,0,-1],[1,1,1],[2,0,0]]
Output: 4
Explanation: The minimum distance between the robot and the target is 4.
Example 3:

Input: grid = [[-1,0],[0,2]]
Output: -1
Explanation: There is no path from the robot to the target cell.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= n, m <= 500
grid[i][j] is either -1, 0, 1, or 2.
There is exactly one -1 in grid.
There is exactly one 2 in grid.
"""
# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        def explore(i, j):
            """
            Explores the grid in a depth first search style.
            Builds a map graph[position] -> {neighbors that are not blocked}.
            If target is found, sets target = (i, j).
            """
            nonlocal visited, target
            pos = (i, j)
            if target is None and master.isTarget():
                target = pos
            visited.add(pos)
            for d in move_map:
                di, dj = move_map[d]
                if master.canMove(d):
                    neigh = (i + di, j + dj)
                    graph[pos].add(neigh)
                    graph[neigh].add(pos)
                    if neigh not in visited:
                        # move into neighbor
                        master.move(d)
                        explore(*neigh)
                        # return from neighbor
                        master.move(return_map[d])
                        
        def bfs(start, target, graph):
            """
            Explores the graph using a level order breadth first search.
            As soon as a path to target is found, returns the number of steps taken.
            """
            q = [start]
            visited = set(q)
            steps = 0
            while q:
                next_level = []
                for pos in q:
                    if pos == target:
                        return steps
                    for neigh in graph[pos]:
                        if neigh not in visited:
                            visited.add(neigh)
                            next_level.append(neigh)
                q = next_level
                steps += 1
            return -1
        
        move_map = {'L': (0,-1),
                    'R': (0,1),
                    'U': (-1,0),
                    'D': (1,0),
                    }
        
        return_map = {'L': 'R',
                      'R': 'L',
                      'U': 'D',
                      'D': 'U',
                      }
        
        start = (0, 0)
        target = None
        graph = collections.defaultdict(set)
        visited = set()
        explore(*start)
        if target is None:
            return -1
        return bfs(start, target, graph)
