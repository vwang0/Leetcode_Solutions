"""
0010. Regular Expression Matching
Hard

5454

830

Add to List

Share
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false
 

Constraints:

0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: 
            return not s
        if not s: 
            return len(p) > 1 and p[1] == '*' and self.isMatch(s, p[2:])
        Matched = (p[0] == '.' or p[0] == s[0])
        if len(p) > 1 and p[1] == '*':
            return (Matched and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        return Matched and self.isMatch(s[1:], p[1:])


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(si, pi):   
            if pi >= len(p): return si == len(s)
            if si >= len(s): return pi + 1 < len(p) and p[pi + 1] == '*' and dp(si, pi + 2)
            if (si, pi) not in memo:
                matched = p[pi] == '.' or p[pi] == s[si]
                if pi + 1 < len(p) and p[pi + 1] == '*':
                    memo[(si, pi)] = dp(si, pi + 2) or (matched and dp(si + 1, pi))
                else:
                    memo[(si, pi)] = matched and dp(si + 1, pi + 1)
            return memo[(si, pi)]
        return dp(0, 0)        