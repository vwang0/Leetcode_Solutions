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
        for i in range((n//2) + 1):
            if num[i] not in table.keys() or table[num[i]] != num[n - i - 1]:
                return False
        return True


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        len2strs = { "00", "11", "88", "69", "96" }
        len1strs = { "0", "1", "8" }
        s = str(num)
        while len(s)>2:
            if s[0]+s[-1] not in len2strs:
                return False
            s = s[1:-1]
        return s in len2strs or s in len1strs

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotates = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        return all(b in rotates and rotates[b] == a
                   for a, b in zip(num, num[::-1]))
