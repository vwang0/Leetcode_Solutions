"""
0238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums)
        lprod = 1
        rprod = 1
        for i in range(len(nums)):
            res[i] *= lprod
            lprod *= nums[i]
            res[~i] *= rprod
            rprod *= nums[~i]
        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        
        res=[0]*len(nums)
        
        if nums.count(0)>1:
            return res
        allpro=1
        
        for num in nums:
            if num !=0 :
                allpro*=num
         
        for i,num in enumerate(nums):
            if num!=0:
                if nums.count(0)==1:
                    res[i]=0
                else: res[i]=int(allpro/num)
            else: res[i]=allpro
        return res