"""
0902. Numbers At Most N Given Digit Set
Hard

Given an array of digits, you can write numbers using each digits[i] as many times as we want.  For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.

 

Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.
Example 3:

Input: digits = ["7"], n = 8
Output: 1
 

Constraints:

1 <= digits.length <= 9
digits[i].length == 1
digits[i] is a digit from '1' to '9'.
All the values in digits are unique.
1 <= n <= 109
"""
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        up, ans, T, str_n = [0]*10, 0, len(digits), str(n)
        for i in range(10):
            for dig in digits:
                up[i] += (dig < str(i))
        
        k, d_set = len(str_n), set(digits)
        for i in range(k):
            if i > 0 and str_n[i-1] not in d_set: break
            ans += up[int(str_n[i])] * T**(k-i-1)
        
        addon = (T**k - 1)//(T-1) - 1 if T != 1 else k - 1
        return ans + addon + (not set(str_n) - set(digits))