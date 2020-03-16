"""
20. Valid Parentheses
Given a string containing just the characters 
'(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""
class Solution(object):
    def isValid(self, s):
        dict1 = {'(': ')', '{': '}', '[': ']'}
        stack1 = []
        for char in s:
            if char in dict1.keys(): 
                stack1.append(char)
            else:
                if not stack1 or dict1[stack1.pop()] != char: 
                    return False
        return not stack1 # return True is stack is empty        


class Solution(object):
    def isValid(self, s):
        left1 = "({["
        right1 = ")}]"
        stack1 = []
        for str in s:
            if str in left1:
                stack1.append(str)
            else:
                if not stack1 or left1.find(stack1.pop()) != right1.find(str):
                    return False
        return not stack1

a = Solution()
a.isValid('([)]')