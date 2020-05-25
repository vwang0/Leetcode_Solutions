"""
0016. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int):
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            if i>=1 and nums[i]==nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            if nums[i]+nums[r-1]+nums[r] <target:
                l = r-1
            elif nums[i]+nums[l]+nums[l+1] >= target:
                r = l+1
            while l<r:
                cur = nums[i]+nums[l]+nums[r]
                if abs(cur-target) < abs(res-target):
                    res =cur
                if cur>target:
                    r-=1
                elif cur<target:
                    l+=1
                else:
                    return target
        return res