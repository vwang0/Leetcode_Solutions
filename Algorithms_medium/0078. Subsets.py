"""
0078. Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution:
    def subsets(self, nums: List[int]):
        res = []
        self.backtracking(res, 0, [], nums)
        return res
    
    def backtracking(self, res, start, subset, nums):
        res.append(list(subset))
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.backtracking(res, i+1, subset, nums)
            subset.pop()
