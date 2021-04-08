"""
1062. Longest Repeating Substring
Medium

Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

 

Example 1:

Input: S = "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: S = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: S = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
Example 4:

Input: S = "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.
 

Constraints:

The string S consists of only lowercase English letters from 'a' - 'z'.
1 <= S.length <= 1500
"""
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        res = 0
        for i in range(1, len(S)):
            if res >= len(S)-i: 
                break                 
            tmp = 0
            for x, y in zip(S[i:],S[:-i]):
                if x == y:
                    tmp += 1 
                    res = max(res, tmp)
                else:
                    tmp = 0             
        return res