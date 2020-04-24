"""
263. Ugly Number
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
Example 1:
Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:
Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:
Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:
1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
"""
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        elif num == 1:
            return True
        q, r = divmod(num, 2)
        if r == 0:
            return self.isUgly(q)
        else:
            q, r = divmod(num, 3)
            if r == 0:
                return self.isUgly(q)
            else:
                q, r = divmod(num, 5)
                if r == 0:
                    return self.isUgly(q)
                else:
                    return False        