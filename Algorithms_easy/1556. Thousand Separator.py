"""
1556. Thousand Separator
Easy

Given an integer n, add a dot (".") as the thousands separator and return it in string format.

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
Example 3:

Input: n = 123456789
Output: "123.456.789"
Example 4:

Input: n = 0
Output: "0"
 
Constraints:

0 <= n < 2^31
"""
class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0: return '0'
        str_n, i = '', 0
        while n:
            i += 1
            str_n = str(n%10) + str_n
            n //= 10
            if i%3 == 0:
                str_n = '.' + str_n
        if str_n[0] == '.': return str_n[1:]
        return str_n