"""
342. Power of Four
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        if num == 1:
            return True
        val = 1
        while val < num:
            val *= 4
            if val == num:
                return True
        return False    
                