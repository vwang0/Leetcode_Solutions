"""
0581. Shortest Unsorted Continuous Subarray
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) :
        sortedNums = sorted(nums)
        start, end = -1, -1
        
        i = 0
        while(i < len(nums)):
            if nums[i] != sortedNums[i]:
                start = i
                break
            i += 1
        if start == -1: return 0 # already sorted
        
        i = len(nums) - 1
        while(i >= 0):
            if nums[i] != sortedNums[i]:
                end = i
                break
            i -= 1
        return end - start + 1


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) :
        return len(''.join(('.', ' ')[m == n] for m, n in zip(sorted(nums), nums)).strip())