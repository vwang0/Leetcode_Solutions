"""
0131. Palindrome Partitioning
Medium

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.helper(s, [], res)
        return res
    
    def helper(self, s, path, res):
        if not s: 
            res.append(path)
            return 
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                self.helper(s[i:], path+[s[:i]], res)
    
