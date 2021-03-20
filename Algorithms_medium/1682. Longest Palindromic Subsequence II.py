"""
1682. Longest Palindromic Subsequence II
Medium

A subsequence of a string s is considered a good palindromic subsequence if:

It is a subsequence of s.
It is a palindrome (has the same value if reversed).
It has an even length.
No two consecutive characters are equal, except the two middle ones.
For example, if s = "abcabcabb", then "abba" is considered a good palindromic subsequence, while "bcb" (not even length) and "bbbb" (has equal consecutive characters) are not.

Given a string s, return the length of the longest good palindromic subsequence in s.

 

Example 1:

Input: s = "bbabab"
Output: 4
Explanation: The longest good palindromic subsequence of s is "baab".
Example 2:

Input: s = "dcbccacdb"
Output: 4
Explanation: The longest good palindromic subsequence of s is "dccd".
 

Constraints:

1 <= s.length <= 250
s consists of lowercase English letters.
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        
        def dp(l, r, prev):
            if (l, r, prev) not in memo:
                if l >= r:
                    return 0
                if s[l] == s[r] and (s[l] != prev):
                    return 2 + dp(l + 1, r - 1, s[l])
                memo[(l, r, prev)] = max(dp(l + 1, r, prev), dp(l, r - 1, prev))
            return memo[(l, r, prev)]
        
        return dp(0, len(s) - 1, '')