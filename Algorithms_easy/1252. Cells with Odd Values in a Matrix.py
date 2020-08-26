"""
1252. Cells with Odd Values in a Matrix
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.

 

Example 1:


Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
Example 2:


Input: n = 2, m = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
 

Constraints:

1 <= n <= 50
1 <= m <= 50
1 <= indices.length <= 100
0 <= indices[i][0] < n
0 <= indices[i][1] < m

"""
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [False] * n
        cols = [False] * m
        for r, c in indices:
            rows[r] = not rows[r]
            cols[c] = not cols[c]
        rows_true = rows.count(True)
        rows_false = n - rows_true
        cols_true = cols.count(True)
        cols_false = m - cols_true
        return rows_true * cols_false + rows_false * cols_true


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        res = 0
        arr = [[0]*m for _ in range(n)]
        for row, col in indices:
            for i in range(m):
                arr[row][i] += 1
            for j in range(n):
                arr[j][col] += 1
        for row in arr:
            for i in row:
                if i%2 ==1:
                    res += 1
        return res
