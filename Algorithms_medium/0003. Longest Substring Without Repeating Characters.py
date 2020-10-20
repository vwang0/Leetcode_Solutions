"""
0003. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str)-> int:
        dic, res, start = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic: 
                res = max(res, i - start)
                start = max(start, dic[ch]+1)
            dic[ch] = i
        return max(res, len(s)-start)


class Solution:
    def lengthOfLongestSubstring(self, s: str)-> int:
        dic, start, length = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                start = max(start, dic[ch]+1)
            dic[ch] = i
            length = max(length, i-start+1)
        return length

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k: 
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res