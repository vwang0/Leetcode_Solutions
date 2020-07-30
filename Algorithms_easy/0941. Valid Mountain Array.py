"""
0941. Valid Mountain Array
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]


 

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
"""
class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length = len(A)
        start, end = 0, length - 1
        while start < length-1 and A[start] < A[start+1]:
            start += 1
        while end > 0 and A[end-1] > A[end]:
            end -= 1
        return start == end and start != 0 and end != length-1


