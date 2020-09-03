"""
Write a function to find continuous ranges in a unsorted list

input: [1, 9, 15 ,20, 30, 4 ,3 ,2, 8, 7 ,21, 16]
output: [[1, 2, 3, 4], [7, 8, 9], [15, 16], [20, 21]]

input: [1, 2, 3, 4]
output: [[1, 2, 3, 4]]

"""

class Solution:
    def findRanges(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp = [nums[0]]
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                temp.append(nums[i])
            else:
                res.append(temp)
                temp = [nums[i]]
        if len(temp) == len(nums):
            return [nums]
        return res


