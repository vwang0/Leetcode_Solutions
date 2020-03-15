"""
1. Two Sum
20200310
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums)<2: 
            return 0
        dict1 = {} 
        for i, num in enumerate(nums):
            if target - num in dict1.keys():
                return (i, dict1[target-num])
            else:
                dict1[num] = i

a = Solution()
a.twoSum([2, 7, 11, 15])
