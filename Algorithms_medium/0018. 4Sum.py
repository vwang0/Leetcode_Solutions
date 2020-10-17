"""
0018. 4Sum
Medium

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
 
Constraints:

0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sumTwo = nums[i] + nums[j]
                d[sumTwo].append((i,j))
        res = set()
        for key in d:
            val = target - key
            if val in d:
                list1 = d[key]
                list2 = d[val]
                for (i, j) in list1:
                    for (k, l) in list2:
                        if len([i,j,k,l]) == len(set([i,j,k,l])):
                            res.add(tuple(sorted([nums[i],nums[j],nums[k],nums[l]])))
        return list(res)            
               
               