"""
0220. Contains Duplicate III
Medium

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int,
                                      t: int) -> bool:
        if t < 0 or not k or not nums:
            return False
        if k == 1:
            for i in range(len(nums) - 1):
                if abs(nums[i] - nums[i + 1]) <= t:
                    return True
            return False

        if not t:
            dct = {}
            for inx, i in enumerate(nums):
                if i in dct:
                    if inx - dct[i] <= k:
                        return True
                dct[i] = inx
            return False

        lst = []
        i = nums[0]
        lst.append(sum([(i - j, i + j) for j in range(t + 1)], ()))

        for i in nums[1:]:
            if i in set(sum(lst, ())):
                return True
            lst.append(sum([(i - j, i + j) for j in range(t + 1)], ()))
            lst = lst[-k:]

        return False
        if t<0 or not k or not nums:
            return False
        if k==1:
            for i in range(len(nums)-1):
                if abs(nums[i] - nums[j+1]) <= t:
                    return True
            return False

        if not t:
            dct = {}
            for inx, i in enumerate(nums):
                if i in dct:
                    if inx-dct[i] <= k:
                        return True
                dct[i] = inx
            return False

        lst = []
        i = nums[0]
        lst.append(sum([(i-j, i+j) for j in range(t+1)], ()))

        for i in nums[1:]:
            if i in set(sum(lst, ())):
                return True
            lst.append(sum([(i-j, i+j) for j in range(t+1)], ()))
            lst = lst[-k:]

        return False
