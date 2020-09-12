"""
0216. Combination Sum III
Medium

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        allNum = [i for i in range(1,10)]
        res = []
        for itm in itertools.combinations(allNum, k):
            if sum(itm) == n:
                res.append(itm)
        return res



class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(list(range(1, 10)), k, n, [], res)
        return res

    def dfs(self, nums, k, n, path, res):
        if k < 0 or n < 0:
            return False
        if k == 0 and n == 0:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], res)


