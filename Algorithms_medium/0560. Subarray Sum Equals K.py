"""
0560. Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        check_sum = defaultdict(int)
        for acc in accumulate(nums, initial=0):
            count += check_sum[acc-k]
            check_sum[acc] += 1
        return count


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        total = {0: 1}
        temp = 0
        for i in range(n):
            temp += nums[i]
            cnt += total.get(temp - k, 0)
            total[temp] = total.get(temp, 0) + 1
        return cnt
