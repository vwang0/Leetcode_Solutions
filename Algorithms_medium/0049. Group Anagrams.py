"""
0049. Group Anagrams
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def convert(s):
            res = [0]*26
            for char in s:
                res[ord(char)-ord('a')] += 1
            return tuple(res)
        rec = {}
        res = []
        for s in strs:
            t = convert(s)
            if t in rec:
                res[rec[t]].append(s)
            else:
                res.append([s])
                rec[t] = len(res)-1
        return res