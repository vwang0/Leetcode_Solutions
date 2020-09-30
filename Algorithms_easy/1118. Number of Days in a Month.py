"""
1118. Number of Days in a Month
Easy

Given a year Y and a month M, return how many days there are in that month.

Example 1:

Input: Y = 1992, M = 7
Output: 31
Example 2:

Input: Y = 2000, M = 2
Output: 29
Example 3:

Input: Y = 1900, M = 2
Output: 28
 
Note:

1583 <= Y <= 2100
1 <= M <= 12
"""
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        up = [1,3,5,7,8,10,12]
        if M<1 or M>12: return 0
        else:
            if M == 2: 
                return 29 if self.leap_year(Y) else 28
            else:
                return 31 if M in up else 30
            
    def leap_year(self,Y):
        if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0): return 1
        else: return 0


