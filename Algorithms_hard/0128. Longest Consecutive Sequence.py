"""
0128. Longest Consecutive Sequence
Hard

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Follow up: Could you implement the O(n) solution? 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                res = max(res, y - x)
        return res