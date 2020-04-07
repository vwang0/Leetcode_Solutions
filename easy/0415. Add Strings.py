"""
415. Add Strings
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ''
        carry = 0
        if len(num1) <= len(num2):
            for i in range(1,len(num1)+1):
                carry, num = divmod(int(num1[-i])+int(num2[-i])+carry, 10)
                num = str(num)
                res = num + res
            for j in range(len(num1)+1, len(num2)+1):
                carry, num = divmod(int(num2[-j])+carry, 10)
                num = str(num)
                res = num + res
            if carry != 0:
                res = str(carry) + res
            return res
        else:
            for i in range(1,len(num2)+1):
                carry, num = divmod(int(num2[-i])+int(num1[-i])+carry, 10)
                num = str(num)
                res = num + res
            for j in range(len(num2)+1, len(num1)+1):
                carry, num = divmod(int(num1[-j])+carry, 10)
                num = str(num)
                res = num + res
            if carry != 0:
                res = str(carry) + res
            return res            
