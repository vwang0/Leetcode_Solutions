"""
0034. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?


Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        cnt = 1
        for idx, num in enumerate(nums):
            if num == target:
                if cnt == 1:
                    res[0] = idx
                    cnt = 2
                if cnt == 2:
                    res[1] = idx
        return res
                
# O(logn) solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def helper(num):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo+hi)//2
                if nums[mid] >= num:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
            
        idx = helper(target)
        return [idx, helper(target+1)-1] if target in nums[idx: idx+1] else [-1, -1]
            
                    
            