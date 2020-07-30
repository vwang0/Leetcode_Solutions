"""
0140. Word Break II
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not wordDict:return []
        max_len = max([len(word) for word in wordDict])
        hashmap = {}
        hashmap = hashmap.fromkeys(wordDict,1)
        memo = {}
        def recur(s):
            if s in memo:return memo[s]
            if s=="":return [""]
            i = 0
            ans = []
            while i <= len(s) and i <= max_len:
                sub = s[:i]
                if hashmap.get(sub,-1)>0:
                    tmp = recur(s[i:])
                    for q in tmp:
                        if q == "":ans.append(sub)
                        else:ans.append(sub+" "+q)
                i += 1
            memo[s] = ans
            return ans

        res = recur(s)
        return res