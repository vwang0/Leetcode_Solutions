"""
0351. Android Unlock Patterns
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

 

Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.
 


 

Explanation:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

 

Example:

Input: m = 1, n = 1
Output: 9
"""
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        cross = collections.Counter({
            (1, 3): 2,
            (3, 1): 2,
            (1, 7): 4,
            (7, 1): 4,
            (3, 9): 6,
            (9, 3): 6,
            (7, 9): 8,
            (9, 7): 8,
            (1, 9): 5,
            (9, 1): 5,
            (2, 8): 5,
            (8, 2): 5,
            (3, 7): 5,
            (7, 3): 5,
            (4, 6): 5,
            (6, 4): 5
        })
        used = [False] * 10

        def dfs(i, k):
            if not k: return 1
            used[i] = True
            cnt = sum(dfs(j, k-1) for j in range(1,10) if not used[j] \
                and (not cross[i,j] or used[cross[i,j]]))
            used[i] = False
            return cnt

        return sum(
            dfs(1, k) * 4 + dfs(2, k) * 4 + dfs(5, k) for k in range(m - 1, n))


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        visited = [False] * 10
        pairs = {(1, 3), (4, 6), (7, 9), (1, 7), (2, 8), (3, 9), (1, 9),
                 (3, 7)}

        def dfs(x, steps):  #return satisfy from this dfs branch.
            if steps > n:
                return 0
            if steps >= m:
                res = 1
            else:
                res = 0
            visited[x] = True
            for y in range(1, 10):
                if not visited[y] and not ((min(x, y), max(x, y)) in pairs
                                           and not visited[(x + y) // 2]):
                    res += dfs(y, steps + 1)
            visited[x] = False
            return res

        return sum(dfs(i, 1) for i in range(1, 10))



class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(10)] for _ in range(10)]
        memo[1][3] = memo[3][1] = 2
        memo[1][9] = memo[9][1] = memo[3][7] = memo[7][3] = memo[2][8] = memo[
            8][2] = memo[4][6] = memo[6][4] = 5
        memo[1][7] = memo[7][1] = 4
        memo[7][9] = memo[9][7] = 8
        memo[3][9] = memo[9][3] = 6

        def helper(path, level):
            if level > n:
                return 0
            temp = 0 if level < m else 1
            for i in range(1, 10):
                if i not in path and (not memo[path[-1]][i]
                                      or memo[path[-1]][i] in path):
                    temp += helper(path + [i], level + 1)
            return temp

        return helper([1], 1) * 4 + helper([2], 1) * 4 + helper([5], 1)




