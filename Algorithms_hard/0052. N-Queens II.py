'''
0052. N-Queens II
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(i):
            if i == n:
                return 1
            res = 0
            for j in range(n):
                if j not in cols and i-j not in diag and i+j not in off_diag:
                    cols.add(j)
                    diag.add(i-j)
                    off_diag.add(i+j)
                    res += backtrack(i+1)
                    off_diag.remove(i+j)
                    diag.remove(i-j)
                    cols.remove(j)
            return res
        cols = set()
        diag = set()
        off_diag = set()
        return backtrack(0)

