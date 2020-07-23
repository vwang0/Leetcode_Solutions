"""
0260. Single Number III
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
class Solution:
    def singleNumber(self, nums: List[int]):
        dict_num, dict_1, res = {}, {}, []
        for num in nums:
            if num not in dict_num:
                dict_num[num] = 1
            else:
                dict_num[num] += 1
        for key in dict_num:
            if dict_num[key] == 1:
                res.append(key)
        return res
