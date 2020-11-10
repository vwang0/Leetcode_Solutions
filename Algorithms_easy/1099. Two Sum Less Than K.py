"""
1099. Two Sum Less Than K
Easy

Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation:
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation:
In this case it's not possible to get a pair sum less that 15.

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        sum2 = float('-inf')
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                temp = A[i] + A[j]
                if temp < K:
                    sum2 = max(sum2, temp)
        return -1 if sum2 == float('-inf') else sum2

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        sum2 = float('-inf')
        for i in range(len(A)):
            for j in range(i, len(A)):
                temp = A[i] + A[j]
                if temp < K:
                    sum2 = max(sum2, temp)
        return sum2 if sum2 != float('-inf') else -1    


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        left, right = 0, len(A)-1
        res = -1
        while left < right:
            total = A[left] + A[right]
            if total < K:
                res = max(res, total)
                left += 1
            else:
                right -= 1
        return res

