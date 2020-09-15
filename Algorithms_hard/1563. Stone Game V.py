"""
1563. Stone Game V
There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's is initially zero.

Return the maximum score that Alice can obtain.

 

Example 1:

Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
Example 2:

Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28
Example 3:

Input: stoneValue = [4]
Output: 0
 

Constraints:

1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 10^6
"""
# O(N^2) solution
from functools import lru_cache
import itertools
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        pre = [0] + list(itertools.accumulate(stoneValue))

        n = len(stoneValue)
        idx = [[0] * n for _ in range(n)]
        for i in range(n):
            idx[i][i] = i
            if i < n - 1:
                idx[i][i + 1] = i
        for i in range(n - 2):
            for j in range(i + 2, n):
                tmp = idx[i][j - 1]
                while pre[tmp + 1] - pre[i] < pre[j + 1] - pre[tmp + 1]:
                    tmp += 1
                idx[i][j] = tmp

        @lru_cache(None)
        def maxL(i, j):
            if i == j: return stoneValue[i]
            return max(maxL(i, j - 1), pre[j + 1] - pre[i] + dp(i, j))

        @lru_cache(None)
        def maxR(i, j):
            if i == j: return stoneValue[i]
            return max(maxR(i + 1, j), pre[j + 1] - pre[i] + dp(i, j))

        @lru_cache(None)
        def dp(i, j):
            if i + 1 == j: return min(stoneValue[i], stoneValue[j])
            mid = idx[i][j]
            res = 0
            if mid > i: res = max(res, maxL(i, mid - 1))
            if mid < j: res = max(res, maxR(mid + 1, j))
            if pre[j + 1] - pre[mid + 1] == pre[mid + 1] - pre[i]:
                res = max(res, maxL(i, mid), maxR(mid + 1, j))
            return res

        return dp(0, n - 1)


#  Below are all O(N^3) solutions

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        acc = [0] + list(itertools.accumulate(stoneValue))

        @functools.lru_cache(None)
        def dfs(i, j):
            if j - i == 1:
                return 0
            ans = 0
            for k in range(i + 1, j):
                s1, s2 = acc[k] - acc[i], acc[j] - acc[k]
                if s1 <= s2:
                    ans = max(ans, dfs(i, k) + s1)
                if s1 >= s2:
                    ans = max(ans, dfs(k, j) + s2)
            return ans

        return dfs(0, n)


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            res = 0
            for k in range(i, j):
                if v[k] - v[i - 1] <= v[j] - v[k]:
                    res = max(res, v[k] - v[i - 1] + dfs(i, k))
                if v[k] - v[i - 1] >= v[j] - v[k]:
                    res = max(res, v[j] - v[k] + dfs(k + 1, j))
            return res

        v = [0] + list(itertools.accumulate(stoneValue))
        return dfs(1, len(v) - 1)


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i, a in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @functools.lru_cache(None)
        def dp(i, j):
            if i == j: return 0
            res = 0
            for m in range(i, j):
                left = prefix[m + 1] - prefix[i]
                right = prefix[j + 1] - prefix[m + 1]
                if left <= right:
                    res = max(res, dp(i, m) + left)
                if left >= right:
                    res = max(res, dp(m + 1, j) + right)
            return res

        return dp(0, n - 1)
