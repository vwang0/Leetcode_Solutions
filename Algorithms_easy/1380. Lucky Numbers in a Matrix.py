"""
1380. Lucky Numbers in a Matrix
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
"""


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]):
        return list(set(min(row) for row in matrix) & set(max(col) for col in zip(*matrix)))


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]):
        row_min = [0 for x in range(len(matrix))]
        col_max = [0 for y in range(len(matrix[0]))]
        matrix_T = []
        result = []
        for i in range(len(matrix)):
            row_min[i] = min(matrix[i])
        for j in range(len(matrix[0])):
            matrix_T.append([z[j] for z in matrix])
        for k in range(len(matrix_T)):
            col_max[k] = max(matrix_T[k])
        for l in range(len(matrix)):
            for m in range(len(matrix[l])):
                if matrix[l][m] == row_min[l] == col_max[m]:
                    result.append(matrix[l][m])
        return result