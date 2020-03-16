"""
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""

class Solution(object):
    def reverse(self, x):
        sign = (x>0) - (x<0)
        res = int(str(sign*x)[::-1])
        y = (res< (1<<31)) * res * sign
        return y

a = Solution()
a.reverse(123)
a.reverse(-123)
a.reverse(120)