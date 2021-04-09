"""
1055. Shortest Way to Form String
Medium

From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        inverted_index = collections.defaultdict(list)
        for i, ch in enumerate(source):
            inverted_index[ch].append(i)

        i, res = -1, 1        
        for ch in target:
            if ch not in inverted_index:
                return -1
            offset_list_for_ch = inverted_index[ch]
            # bisect_left(A, x) returns the smallest index j s.t. A[j] >= x. If no such index j exists, it returns len(A).
            j = bisect.bisect_left(offset_list_for_ch, i)
            if j == len(offset_list_for_ch):
                res += 1
                i = offset_list_for_ch[0] + 1
            else:
                i = offset_list_for_ch[j] + 1

        return res