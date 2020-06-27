"""
0279. Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
class Solution:
    def numSquares(self, n: int):
        if n == 0: return 0
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, i*i):
                if i - j*j < 0:
                    break
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[-1]




