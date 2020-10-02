"""
0039. Combination Sum
Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]
 
Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)
        
        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
                return result
            for item in candidates:
                if item > remain: break
                if stack and item < stack[-1]: continue
                else:
                    dfs(remain - item, stack + [item])
                                                        
        dfs(target, [])
        return result



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)


