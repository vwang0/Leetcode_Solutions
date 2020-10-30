"""
0673. Number of Longest Increasing Subsequence
Medium

Given an integer array nums, return the number of longest increasing subsequences.

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.


Constraints:

0 <= nums.length <= 2000
-106 <= nums[i] <= 106
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = []
        num_sequences_of_length = collections.defaultdict(list)
        for i in range(len(nums)):
            pos = bisect_left(dp, nums[i])
            if pos == len(dp):
                dp.append(nums[i])
            else:
                dp[pos] = nums[i]
            total = 0
            for count, last in num_sequences_of_length[pos]:
                if last < nums[i]:
                    total += count
            num_sequences_of_length[pos+1].append((max(1, total), nums[i]))
        return sum([count for count,_ in num_sequences_of_length[len(dp)]])
