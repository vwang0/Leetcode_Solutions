"""
45. Jump Game II
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:
You can assume that you can always reach the last index.
"""
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_jump = 0
        far, max_dis = 0, 0
        for i, num in enumerate(nums):
            max_dis = max(max_dis, num+i)
            if far<=i and i<len(nums)-1:
                num_jump+=1
                far = max_dis
            
        return num_jump

class Solution:        
    def jump(self, nums):
        if not nums or len(nums) == 1:
            return 0

        des = len(nums) - 1
        res = 0
        i = 0
        max_range = 0
        nxt = 0
        while i < des:
            if i + nums[i] >= des:
                return res + 1
            for r in range(i + 1, i + nums[i] + 1):
                if r + nums[r] > max_range:
                    max_range = r + nums[r]
                    nxt = r
            i = nxt
            res += 1
    