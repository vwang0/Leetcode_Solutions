"""
0072. Edit Distance
Hard

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        # if one of the strings is empty
        if n * m == 0:
            return n + m
        
        # array to store the convertion history
        d = [ [0] * (m + 1) for _ in range(n + 1)]
        
        # init boundaries
        for i in range(n + 1):
            d[i][0] = i
        for j in range(m + 1):
            d[0][j] = j
        
        # DP compute 
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = d[i - 1][j] + 1
                down = d[i][j - 1] + 1
                left_down = d[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                d[i][j] = min(left, down, left_down)
        
        return d[n][m]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1, word2 = "!" + word1, "!" + word2
        n_1, n_2 = len(word1), len(word2)
        dp = [[0] * n_2 for _ in range(n_1)]
        for i_1 in range(n_1): dp[i_1][0] = i_1
        for i_2 in range(n_2): dp[0][i_2] = i_2
        for i_1 in range(1, n_1):
            for i_2 in range(1,n_2):
                Cost = (word1[i_1] != word2[i_2])
                dp[i_1][i_2] = min(dp[i_1-1][i_2] + 1, dp[i_1][i_2-1] + 1, dp[i_1-1][i_2-1] + Cost)
        return int(dp[-1][-1])
