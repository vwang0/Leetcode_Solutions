"""
88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
# Solution 1:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        return nums1

# Solution 2:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        l1, l2, end = m-1, n-1, m+n-1
        while l1 >= 0 and l2 >= 0:
            if nums2[l2] > nums1[l1]:
                nums1[end] = nums2[l2]
                l2 -= 1
            else:
                nums1[end] = nums1[l1]
                l1 -= 1
            end -= 1
        if l1 < 0: # if nums2 left
            nums1[:l2+1] = nums2[:l2+1]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        m, n = m-1, n-1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[m+n+1] = nums1[m]
                m -= 1
            else:
                nums1[m+n+1] = nums2[n]
                n -= 1
        if n != -1: # nums2 is still left
            nums1[:n+1] = nums2[:n+1]