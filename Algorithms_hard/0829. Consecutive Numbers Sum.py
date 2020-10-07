"""
0829. Consecutive Numbers Sum
Hard

Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
"""
"""
N can be expressed as k, k + 1, k + 2, ..., k + (i - 1), 
where k is a positive integer; therefore

N = k * i + (i - 1) * i / 2 => N - (i - 1) * i / 2 = k * i, 
which implies that as long as N - (i - 1) * i / 2 is k times of i, 
we get a solution corresponding to i; 
Hence iteration of all possible values of i, starting from 1, 
will cover all cases of the problem.
"""
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        i, res = 1, 0
        while N > i*(i-1)//2:
            if (N - i*(i-1)//2) % i == 0:
                res += 1
            i += 1
        return res
    