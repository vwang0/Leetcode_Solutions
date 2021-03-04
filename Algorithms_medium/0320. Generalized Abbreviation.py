"""
0320. Generalized Abbreviation
Medium

A word's generalized abbreviation can be constructed by taking any number of non-overlapping substrings and replacing them with their respective lengths. For example, "abcde" can be abbreviated into "a3e" ("bcd" turned into "3"), "1bcd1" ("a" and "e" both turned into "1"), and "23" ("ab" turned into "2" and "cde" turned into "3").

Given a string word, return a list of all the possible generalized abbreviations of word. Return the answer in any order.

 

Example 1:

Input: word = "word"
Output: ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]
Example 2:

Input: word = "a"
Output: ["1","a"]
 

Constraints:

1 <= word.length <= 15
word consists of only lowercase English letters.
"""
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def helper(word, pos, cur, count, result):
            if len(word) == pos:
                # Once we reach the end, append current to the result
                result.append(cur + str(count) if count > 0 else cur)
            else:
                # Skip current position, and increment count
                helper(word, pos + 1, cur, count + 1, result)
                # Include current position, and zero-out count
                helper(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, result)

        result = []
        helper(word, 0, '', 0, result)
        return result