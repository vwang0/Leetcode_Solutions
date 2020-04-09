"""
345. Reverse Vowels of a String
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        ls = list(s)
        vowels = {'a', 'e', 'u', 'i', 'o'}
        l, r = 0, len(ls) - 1
        while l < r:
            while l < r and ls[l].lower() not in vowels:
                l += 1
            while l < r and ls[r].lower() not in vowels:
                r -= 1
            ls[l], ls[r] = ls[r], ls[l]
            l += 1
            r -= 1
        return ''.join(ls)
