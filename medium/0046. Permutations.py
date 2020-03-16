"""
46. Permutations
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        answer = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for perm in self.permute(n):
                answer.append([num] + perm)
        return answer

class Solution(object):
    def permute(self, nums):
        return [[n] + p for i, n in enumerate(nums) for p in self.permute(nums[:i]+ nums[i+1:])] or [[]]

