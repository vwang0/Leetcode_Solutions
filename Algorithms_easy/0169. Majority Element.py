"""
169. Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max(cnt.keys(), key=cnt.get)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for num in nums:
            if dic[num] > len(nums) // 2:
                return num
