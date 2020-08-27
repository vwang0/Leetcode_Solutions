"""
680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        while i < len(s) // 2 and s[i] == s[-(i + 1)]:
            i += 1
        ss = s[i:len(s) - i]
        return ss[1:] == ss[1:][::-1] or ss[:-1] == ss[:-1][::-1]


