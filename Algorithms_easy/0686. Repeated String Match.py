"""
0686. Repeated String Match

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        num_rpt = len(B)//len(A)+1+1
        i = 1
        while i <= num_rpt:
            if B in A*i:
                return i
            i +=1
        return -1