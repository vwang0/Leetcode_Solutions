"""
0186. Reverse Words in a String II
Medium

Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

 

Example 1:

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:

Input: s = ["a"]
Output: ["a"]
 

Constraints:

1 <= s.length <= 105
s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
There is at least one word in s.
s does not contain leading or trailing spaces.
All the words in s are guaranteed to be separated by a single space.
 

Follow up: Could you do it in-place without allocating extra space?
"""
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)
        beg = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse(s, beg, i-1)
                beg = i + 1
            elif i == len(s) - 1:
                self.reverse(s, beg, i)
        
    def reverse(self, s, start,end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1