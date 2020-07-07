"""
0697. Degree of an Array
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dict = {}
        dp = [0] * (max(nums)+1)
        for i,j in enumerate(nums):   
            dict[j] = i     
            dp[j] += 1       
        max_=max(dp)
        min_=float("inf")
        for i in range(len(dp)):
            if dp[i] == max_:     
                b=dict[i]      
                c=nums.index(i)   
                d=b-c+1           
                min_ = min(min_,d)
        return min_
        
