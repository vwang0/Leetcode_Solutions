'''
0047. Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) ==: return [[]]
        res = [[]]
        for n in nums:
            temp=[]
            for r in res:
                for i in range(len(r)+1):
                    temp.append(r[:i]+[n]+r[i:])
                    if i<len(r) and r[i]==n: break
            res=temp
        return res
