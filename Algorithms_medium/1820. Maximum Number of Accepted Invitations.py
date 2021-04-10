"""
1820. Maximum Number of Accepted Invitations
Medium

There are m boys and n girls in a class attending an upcoming party.

You are given an m x n integer matrix grid, where grid[i][j] equals 0 or 1. If grid[i][j] == 1, then that means the ith boy can invite the jth girl to the party. A boy can invite at most one girl, and a girl can accept at most one invitation from a boy.

Return the maximum possible number of accepted invitations.

 

Example 1:

Input: grid = [[1,1,1],
               [1,0,1],
               [0,0,1]]
Output: 3
Explanation: The invitations are sent as follows:
- The 1st boy invites the 2nd girl.
- The 2nd boy invites the 1st girl.
- The 3rd boy invites the 3rd girl.
Example 2:

Input: grid = [[1,0,1,0],
               [1,0,0,0],
               [0,0,1,0],
               [1,1,1,0]]
Output: 3
Explanation: The invitations are sent as follows:
-The 1st boy invites the 3rd girl.
-The 2nd boy invites the 1st girl.
-The 3rd boy invites no one.
-The 4th boy invites the 2nd girl.
 

Constraints:

grid.length == m
grid[i].length == n
1 <= m, n <= 200
grid[i][j] is either 0 or 1.
"""
class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        matching = [-1] * N # girls' mate
        
        def dfs(node, seen):
            for nei in range(N): # ask each girl
                if grid[node][nei] and not seen[nei]: 
                    seen[nei] = True # mark her as asked
                    if matching[nei] == -1 or dfs(matching[nei], seen): 
                        matching[nei] = node 
                        return True
            return False
    
        res = 0
        for i in range(M):
            seen = [False] * N
            if dfs(i, seen):
                res += 1                
        return res