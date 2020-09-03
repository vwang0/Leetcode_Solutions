"""
0758. Bold Words in String
Easy

Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Constraints:

words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
All characters in words[i] and S are lowercase letters.
Note: This question is the same as 616: https://leetcode.com/problems/add-bold-tag-in-string/

"""
class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        n = len(S)
        b = [False] * n
        for w in words:
            t = S.find(w)
            length = len(w)
            while t > -1:
                for i in range(t, t + length):
                    b[i] = True
                t = S.find(w, t + 1)
        res = ''
        i = 0
        while i < n:
            if b[i]:
                res += r'<b>'
                while i < n and b[i]:
                    res += S[i]
                    i += 1
                res += r'</b>'
            else:
                res += S[i]
                i += 1
        return res



