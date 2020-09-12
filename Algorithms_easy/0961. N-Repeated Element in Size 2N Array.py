"""
0961. N-Repeated Element in Size 2N Array
Easy

In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5
 

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A) // 2
        cnt = collections.Counter(A)
        for itm in cnt:
            if cnt[itm] == N:
                return itm


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        while 1:
            smp = random.sample(A, 2)
            if smp[0] == smp[1]:
                return smp[0]


                