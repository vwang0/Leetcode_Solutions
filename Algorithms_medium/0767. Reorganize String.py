"""
0767. Reorganize String
Medium

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
class Solution:
    def reorganizeString(self, S: str) -> str:
        L = sorted(sorted(S), key = S.count)
        half = len(L) // 2
        L[1::2], L[::2] = L[:half], L[half:]
        return ''.join(L) * (L[-1:] != L[-2:-1])
        