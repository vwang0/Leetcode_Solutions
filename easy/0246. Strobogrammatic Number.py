"""
246. Strobogrammatic Number
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is strobogrammatic. The number is represented as a string.
Example 1:
Input:  "69"
Output: true
Example 2:
Input:  "88"
Output: true
Example 3:
Input:  "962"
Output: false
"""
class Solution(object):
    def isStrobogrammatic(self, num):
        table = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        n = len(num)
        for i in range((n >> 1) + 1):
            if num[i] not in table or table[num[i]] != num[n - i - 1]:
                return False
        return True
