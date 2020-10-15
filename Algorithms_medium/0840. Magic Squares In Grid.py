"""
0840. Magic Squares In Grid
Easy

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def isMagic(i, j):
            s = "".join(
                str(grid[i + x // 3][j + x % 3])
                for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return grid[i][j] % 2 == 0 and (s in "43816729" * 2
                                            or s in "43816729" [::-1] * 2)

        return sum(
            isMagic(i, j) for i in range(len(grid) - 2)
            for j in range(len(grid[0]) - 2) if grid[i + 1][j + 1] == 5)
