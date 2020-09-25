"""
179. Largest Number
Medium

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numL = sorted([str(num) for num in nums],
                      key=functools.cmp_to_key(lambda b, a: (
                          (a + b) > (b + a)) - ((a + b) < (b + a))))
        res = ''.join(numL)
        return res.lstrip('0') or '0'


