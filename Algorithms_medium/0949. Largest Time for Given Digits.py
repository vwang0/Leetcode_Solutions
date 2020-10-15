"""
0949. Largest Time for Given Digits

Easy

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
 

Note:

A.length == 4
0 <= A[i] <= 9
"""


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        for p in itertools.permutations(sorted(A, reverse=True)):
            if p[0] * 10 + p[1] < 24 and p[2] < 6:
                return f"{p[0]}{p[1]}:{p[2]}{p[3]}"
        return ''


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        return max(['%d%d:%d%d' % t for t in itertools.permutations(A) if t[:2] < (2,4) and t[2] < 6] or [""])