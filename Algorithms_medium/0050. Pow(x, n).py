"""
0050. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""
class Solution:
    def myPow(self, x: float, n: int) :
        def calc(x, y):
            if y == 0:
                return 1
            if y == 1:
                return x
            if y % 2:
                return x * calc(x, y - 1)
            return calc(x * x, y // 2)

        if n < 0:
            return calc((1 / x), -1 * n)
        else:
            return calc(x, n)
