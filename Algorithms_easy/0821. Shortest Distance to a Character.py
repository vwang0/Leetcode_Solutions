"""
0821. Shortest Distance to a Character
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        res = [0 if s==C else n for s in S]
        for i in range(1,n):
            res[i] = min(res[i], res[i-1]+1)
        for i in range(n-2, -1, -1):
            res[i] = min(res[i], res[i+1]+1)
        return res