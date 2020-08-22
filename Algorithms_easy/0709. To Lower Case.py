"""
0709. To Lower Case
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""

class Solution:
    def toLowerCase(self, str: str) -> str:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        hashmap = dict(zip(upper, lower))
        return ''.join(hashmap[x] if x in hashmap else x for x in str)


class Solution:
    def toLowerCase(self, str: str) -> str:
        is_upper = lambda x: 'A' <= x <= 'Z'
        to_lower = lambda x: chr(ord(x) | 32)
        return ''.join(to_lower(x) if is_upper(x) else x for x in str)
