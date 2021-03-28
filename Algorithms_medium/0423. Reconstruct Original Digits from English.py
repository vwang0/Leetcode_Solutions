"""
0423. Reconstruct Original Digits from English
Medium

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
"""
class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)
        Digits = ["zero","two","four","six","eight","one","three","five","seven","nine"]
        Corresp = [0,2,4,6,8,1,3,5,7,9]
        Counters = [Counter(digit) for digit in Digits]
        Found = [0]*10
        for it, C in enumerate(Counters):
            k = min(cnt[x]//C[x] for x in C)
            for i in C.keys(): C[i] *= k
            cnt -= C
            Found[Corresp[it]] = k
            
        return "".join([str(i)*Found[i] for i in range(10)])     