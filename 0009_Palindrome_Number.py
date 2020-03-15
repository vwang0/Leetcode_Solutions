"""
9. Palindrome Number

Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. 
From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. 
Therefore it is not a palindrome.
"""
class Solution:
    def isPalindrome(self, x) :
        if x >= 0:
            str_x = str(x)
            str_x = str_x[::-1]
            y = int(str_x)
        else:
            return 0
        return x == y