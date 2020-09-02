"""
0747. Largest Number At Least Twice of Others
Easy
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
 

Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
"""


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1
        highest = -1
        secondHighest = -1
        highestIndex = 0
        for idx, num in enumerate(nums):
            if num >= highest:
                secondHighest = highest
                highest = num
                highestIndex = idx
            elif num > secondHighest:
                secondHighest = num
        if highest >= 2 * secondHighest:
            return highestIndex
        return -1


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1
        max_num = max(nums)
        for num in nums:
            if num != max_num and num != 0 and max_num // num < 2:
                return -1
        return nums.index(max_num)
