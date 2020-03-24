"""
276. Paint Fence
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3      
 -----      -----  -----  -----       
   1         c1     c1     c2 
   2         c1     c2     c1 
   3         c1     c2     c2 
   4         c2     c1     c1  
   5         c2     c1     c2
   6         c2     c2     c1
"""
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int, number of posts
        :type k: int, number of colors
        :rtype: int
        """
        if n==0 or k==0:
            return 0

        lastSame = 0 # number of ways where last 2 posts have same color
        lastDiff = k # number of ways where last 2 posts have different colors

        for m in range(n-1):
            newLastSame = lastDiff
            newLastDiff = ( lastSame + lastDiff ) * ( k - 1 )
            lastSame, lastDiff = newLastSame, newLastDiff

        return lastSame + lastDiff

class Solution(object):
    def numWays(self, n, k):
        if n <= 0 or k <= 0:
            return 0

        dp = [0] * n

        dp[0] = k
        if n > 1:
            dp[1] = k * k

        for i in range(2, n):
            dp[i] = dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)

        return dp[n - 1]