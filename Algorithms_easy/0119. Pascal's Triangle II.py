"""
119. Pascal's Triangle II
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [[1 for _ in range(i+1)] for i in range(rowIndex+1)]
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res[rowIndex]