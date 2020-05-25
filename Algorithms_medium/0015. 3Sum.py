"""
0015. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums: List[int]) :
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>=1 and nums[i]==nums[i-1]: 
                continue
            target = -nums[i]
            cache = set()
            for j in range(i+1, len(nums)): 
                if nums[j] in cache:
                    if len(res) == 0 or res[-1]!=[nums[i],target-nums[j],nums[j]]:
                        res.append([nums[i],target-nums[j],nums[j]])
                cache.add(target-nums[j])
        return res