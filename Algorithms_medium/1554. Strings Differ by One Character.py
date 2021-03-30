"""
1554. Strings Differ by One Character
Medium

Given a list of strings dict where all the strings are of the same length.

Return True if there are 2 strings that only differ by 1 character in the same index, otherwise return False.

Follow up: Could you solve this problem in O(n*m) where n is the length of dict and m is the length of each string.

 

Example 1:

Input: dict = ["abcd","acbd", "aacd"]
Output: true
Explanation: Strings "abcd" and "aacd" differ only by one character in the index 1.
Example 2:

Input: dict = ["ab","cd","yz"]
Output: false
Example 3:

Input: dict = ["abcd","cccc","abyd","abab"]
Output: true
 

Constraints:

Number of characters in dict <= 10^5
dict[i].length == dict[j].length
dict[i] should be unique.
dict[i] contains only lowercase English letters.
"""
class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        n, m = len(dict), len(dict[0])
        for j in range(m):
            seen = set()
            for i in range(n):
                new_w = dict[i][:j] + '*' +dict[i][j+1:]
                if new_w in seen:
                    return True
                seen.add(new_w)
        return False