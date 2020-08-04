"""
0414. Third Maximum Number
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""
class Solution:
    def thirdMax(self, nums: List[int]):
        pre, cur, maxlen = -1, 0, 0
        for num in nums:
            if num == 0:
                pre, cur = cur, 0
            else:
                cur += 1
            maxlen = max(maxlen, pre+1+cur)
        return maxlen

        