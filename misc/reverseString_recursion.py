"""
reverse string with recursion

"""
class Solution:
    def reverseString(self, s: List[str]):
        """
        Do not return anything, modify s in-place instead.
        """
    def helper(start, end, ls):
        if start >= end:
            return
        ls[start], ls[end] = ls[end], ls[start]
    return helper(0, len(s)-1, s)


class Solution:
    def reverseString(self, s: List[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i], s[n-1-i] = s[n-1-i], s[i]

    