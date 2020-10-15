"""
1108. Defanging an IP Address
Easy

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 
Constraints:

The given address is a valid IPv4 address.
"""
class Solution:
    def defangIPaddr(self, address: str) -> str:
        d_ip = ""
        # d_ip=address.replace('.','[.]')
        
        for i in address:
            if(i == '.'):
                d_ip += '[.]'
            else:
                d_ip += i
                
        return d_ip