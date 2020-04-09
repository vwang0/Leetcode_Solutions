"""
383. Ransom Note
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
Note:
You may assume that both strings contain only lowercase letters.
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        return not Counter(ransomNote) - Counter(magazine)

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        letters = Counter(magazine)
        for char in ransomNote:
            if char not in letters.keys():
                return False
            else:
                letters[char] -= 1
                if letters[char] < 0:
                    return False 
        return True            