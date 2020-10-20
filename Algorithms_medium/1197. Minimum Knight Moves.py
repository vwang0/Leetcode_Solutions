"""
1197. Minimum Knight Moves
Medium

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

|x| + |y| <= 300
"""
from functools import lru_cache
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(None) 
        def DP(x,y):
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            return min(DP(abs(x-1),abs(y-2)),DP(abs(x-2),abs(y-1)))+1
        return DP(abs(x),abs(y))        

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        cache = {(0, 0): 0, (1, 0): 3, (0, 1): 3, (1, 1): 2}        
        def dfs(x, y):
            if (x, y) in cache: return cache[(x, y)]
            res = min(dfs(abs(x-1), abs(y-2)), dfs(abs(x-2), abs(y-1))) + 1
            cache[(x, y)] = res
            return res
        return dfs(abs(x), abs(y))