"""
0594. Longest Harmonious Subsequence
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
"""
class Solution:
    def findLHS(self, nums: List[int]):
        dic = {}
        res = 0
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key in dic:
            if key + 1 in dic:
                res = max(res, dic[key] + dic[key+1])
        return res
