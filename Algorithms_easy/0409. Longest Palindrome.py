"""
409. Longest Palindrome
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Note:
Assume the length of given string will not exceed 1,010.
Example:
Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
保留所有偶数个字母c: 4, d:2，只保留一个奇数个字母a，或者保留奇数个字母里面成对的，比如eee, 保留ee
"""
from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = Counter(s)
        res = 0
        flag = False
        for key, val in dic.items():
            if val % 2 == 0:
                res += val
            else:
                if flag:
                    res += val-1
                else:
                    flag = True
                    res += val
        return res