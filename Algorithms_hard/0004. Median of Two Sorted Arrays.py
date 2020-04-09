"""
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
from math import floor
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = floor((m + n - 1) / 2)
        lo, hi = 0, m
        while lo < hi:
            i = floor((lo + hi) / 2)
            j = after - i
            cond1 = (j>=1 and a[i] >= b[j-1]) or j==0
            cond2 = (i>=1 and b[j] >= a[i-1]) or i==0
            if(cond1 and cond2):
                lo = i
                break
            elif(not cond1):
                lo = i + 1
            else:
                hi = i
        i = lo
        j = after - i

        nextfew = sorted(a[i:i+2] + b[j:j+2])
        return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0

