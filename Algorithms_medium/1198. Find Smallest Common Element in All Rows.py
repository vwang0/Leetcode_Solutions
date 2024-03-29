"""
1198. Find Smallest Common Element in All Rows
Medium

Given a matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

 

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
 

Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in strictly increasing order.
"""
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        c = collections.Counter()
        for row in mat:
            for a in row:
                c[a] += 1
                if c[a] == len(mat):
                    return a
        return -1