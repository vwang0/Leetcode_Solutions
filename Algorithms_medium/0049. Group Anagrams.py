"""
0049. Group Anagrams
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert(s):
            res = [0] * 26
            for ch in s:
                res[ord(ch) - ord('a')] += 1
            return tuple(res)
        
        cnt = {}
        res = []
        for s in strs:
            t = convert(s)
            if t in cnt:
                res[cnt[t]].append(s)
            else:
                res.append([s])
                cnt[t] = len(res) - 1
        return res