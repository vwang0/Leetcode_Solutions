"""
0421. Maximum XOR of Two Numbers in an Array
Medium

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for i in reversed(range(32)):
            prefixes = set([x >> i for x in nums])
            res <<= 1
            candidate = res + 1
            for p in prefixes:
                if candidate ^ p in prefixes:
                    res = candidate
                    break
        return res

