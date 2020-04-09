"""
168. Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""
class Solution(object):
    def convertToTitle(self, n):
        dict1 =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res1 = ''
        while n > 0:
            n, rem = divmod(n-1, 26)
            res1 = dict1[rem] + res1
        return res1

