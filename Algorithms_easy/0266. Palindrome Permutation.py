"""
266. Palindrome Permutation
Given a string, determine if a permutation of the string could form a palindrome.
Palindrome is a word that spells forward and backward the same.
Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""
class Solution:
    def canPermutePalind(self, s):
        CharSet = set()
        for c in s: 
            if c in CharSet:
                CharSet.remove(c)
            else:
                CharSet.add(c)
        return len(CharSet)<=1