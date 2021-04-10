"""
0562. Longest Line of Consecutive One in Matrix
Medium

Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
"""
class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        maxlen = 0
        currlen = collections.Counter()
        for i, row in enumerate(M):
            for j, a in enumerate(row):
                for key in i, j+.1, i+j+.2, i-j+.3:
                    currlen[key] = (currlen[key] + 1) * a
                    maxlen = max(maxlen, currlen[key])
        return maxlen