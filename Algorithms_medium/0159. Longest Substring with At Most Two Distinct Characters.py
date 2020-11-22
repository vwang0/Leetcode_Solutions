"""
0159. Longest Substring with At Most Two Distinct Characters
Medium

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, longest, d = 0, 0, {}
        maximum_distinct = 2
        for index, char in list(enumerate(s)):
            d[char] = index
            if len(d.keys()) == maximum_distinct + 1:
                index_to_remove = min([d[char] for char in d.keys()])
                d.pop(s[index_to_remove], None)
                left = index_to_remove + 1
            longest = max(longest, index - left + 1)
        return longest