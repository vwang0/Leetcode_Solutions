"""
0996. Number of Squareful Arrays
Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

 

Example 1:

Input: [1,17,8]
Output: 2
Explanation: 
[1,8,17] and [17,8,1] are the valid permutations.
Example 2:

Input: [2,2,2]
Output: 1
 

Note:

1 <= A.length <= 12
0 <= A[i] <= 1e9
"""
def numSquarefulPerms(self, A):
    c = collections.Counter(A)
    cand = {i: {j for j in c if int((i + j)**0.5) ** 2 == i + j} for i in c}

    def dfs(x, left=len(A) - 1):
        c[x] -= 1
        count = sum(dfs(y, left - 1) for y in cand[x] if c[y]) if left else 1
        c[x] += 1
        return count
    return sum(map(dfs, c))


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        
        A.sort()
        self.ans = 0
        
        # using permutation 
        def dfs(A, path):
            if len(A)==0:
                self.ans+=1
                return 

            for i in range(len(A)):
                if i>0 and A[i]==A[i-1]:
                    continue
                if len(path)==0 or (len(path)>0 and int((A[i]+path[-1])**0.5+0.0)**2==A[i]+path[-1]):
                    dfs(A[:i]+A[i+1:], path+[A[i]])
                    
        dfs(A, [])
        return self.ans 