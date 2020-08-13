"""
0507. Perfect Number
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
"""
class Solution:
    def checkPerfectNumber(self, num: int):
        if num <= 1: return False
        sqrt_num = int(sqrt(num))
        total = 1
        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                total += (i + num // i)
        return num == total