"""
1572. Matrix Diagonal Sum
Easy
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
 

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
"""


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        pri_diag, sec_diag = 0, 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    pri_diag += mat[i][j]
                if i + j == (n - 1) and i != j:
                    sec_diag += mat[i][j]
        res = pri_diag + sec_diag
        return res


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l, r, res = 0, len(mat[0]) - 1, 0

        for row in mat:
            if l != r:
                res += row[l]
                res += row[r]
            else:
                res += row[l]
            l += 1
            r -= 1

        return res

        
