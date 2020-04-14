"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum 
and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
If you have figured out the O(n) solution, try coding another 
solution using the divide and conquer approach, which is more subtle.
"""
class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0

        cumSum = maxSum = nums[0]
        for num in nums[1:]:
            cumSum = max(num, cumSum + num)
            maxSum = max(maxSum, cumSum)

        return maxSum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        sm, mn, mx = 0, 0, -float('inf')
        for num in nums:
            sm += num
            mx, mn = max(mx, sm-mn), min(mn,sm)
        return mx