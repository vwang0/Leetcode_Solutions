"""
0368. Largest Divisible Subset
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]

"""
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The container that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        subsets = {-1: set()}
        
        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
        
        return list(max(subsets.values(), key=len))


class Solution(object):
        def largestDivisibleSubset(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            if not nums:
                return []
            nums=sorted(nums)
            cont=[1]*len(nums)
            par=[-1]*len(nums)
            m,mi=0,-1
            for i in xrange(len(nums)):
                for j in xrange(i):
                    if not nums[i]%nums[j] and cont[i]<=cont[j]:
                        cont[i]=cont[j]+1
                        par[i]=j
                if cont[i]>m:
                    m,mi=cont[i],i
            ans=[]
            while mi>=0:
                ans.append(nums[mi])
                mi=par[mi]
            return ans