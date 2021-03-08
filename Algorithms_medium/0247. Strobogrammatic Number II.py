"""
0247. Strobogrammatic Number II
Medium


Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]
 

Constraints:

1 <= n <= 14
"""
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        evenMidCand = ["11","69","88","96", "00"]
        oddMidCand = ["0", "1", "8"]
        if n == 1:
            return oddMidCand
        if n == 2:
            return evenMidCand[:-1]
        if n % 2:
            pre, midCand = self.findStrobogrammatic(n-1), oddMidCand
        else: 
            pre, midCand = self.findStrobogrammatic(n-2), evenMidCand
        premid = (n-1)//2
        return [p[:premid] + c + p[premid:] for c in midCand for p in pre]


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        nums = n%2 * list('018') or ['']
        while n > 1:
            n -= 2
            nums = [a + num + b for a, b in '00 11 88 69 96'.split()[n<2:] for num in nums]
        return nums