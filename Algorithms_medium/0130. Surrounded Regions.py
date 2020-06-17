"""
0130. Surrounded Regions
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(y, x):
            seen[y][x] = 1
            board[y][x] = 'N'
            if y > 0 and board[y-1][x] == 'O' and  seen[y-1][x] == 0:
                dfs(y-1, x)
            if y < len(board)-1 and board[y+1][x] == 'O' and seen[y+1][x] == 0:
                dfs(y+1, x)
            if x > 0 and board[y][x-1] == 'O' and seen[y][x-1] == 0:
                dfs(y, x-1)
            if x < len(board[0])-1 and board[y][x+1] == 'O' and seen[y][x+1] == 0:
                dfs(y, x+1)
        
        if not board or not board[0]:
            return
        seen = [[0]*len(board[0]) for _ in range(len(board))]
        for j in range(len(board[0])):
            if board[0][j] == "O" and seen[0][j] == 0:
                dfs(0, j)
            if board[len(board)-1][j] == "O" and seen[len(board)-1][j] == 0:
                dfs(len(board)-1, j)
        for i in range(len(board)):
            if board[i][0] == "O" and seen[i][0] == 0:
                dfs(i, 0)
            if board[i][len(board[0])-1] == "O" and seen[i][len(board[0])-1] == 0:
                dfs(i, len(board[0])-1)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "N":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"        