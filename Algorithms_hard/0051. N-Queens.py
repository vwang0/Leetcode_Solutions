'''
0051. N-Queens
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return [['.' * v + 'Q' + '.' * (n - v - 1) for v in c] for c in itertools.permutations(range(n))
                if (len(set(i + v for i, v in enumerate(c))) == n) and
                (len(set(i - v for i, v in enumerate(c))) == n)]
