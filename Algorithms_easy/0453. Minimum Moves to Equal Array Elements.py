"""
0453. Minimum Moves to Equal Array Elements
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

m moves reach final value x, and each move increments length - 1 elements
sum(nums) + m * (len(nums)-1) = x * len(nums)
min(nums) + m = x
So，
sum(nums) + m * (len(nums)-1) = (min(nums) + m) * len(nums)
sum(nums) - m  = min(nums) * len(nums)
m = sum(nums) - min(nums) * len(nums)
"""

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)