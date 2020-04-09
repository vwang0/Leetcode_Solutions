"""
367. Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""
class Solution:
    def isPerfectSquare(self, num: int):
        # (a+1)^2 - a^2 = 2*a + 1
        if num<0:
            return False
        x,i = 0,1
        while x<num:
            x += i
            i += 2
        return x == num        

class Solution:
   def isPerfectSquare(self, num: int):
        if num < 1: return False
        if num == 1: return True
        left, right = 0, num
        while left < right:
            mid = (left+right)//2
            if mid > num/mid:
                right = mid - 1
            elif mid == num/mid:
                return True
            else:
                left = mid + 1
        return left == num//left and num%left == 0 