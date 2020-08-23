"""
349. Intersection of Two Arrays
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        hashmap = dict()
        for num in nums1:
            hashmap[num] = hashmap.get(num, 0) + 1
        for j in nums2:
            if j in hashmap and hashmap[j] > 0:
                res.append(j)
                hashmap[j] = 0
        return res


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snum1 = set(nums1)
        snum2 = set(nums2)
        return list(snum1.intersection(nums2))