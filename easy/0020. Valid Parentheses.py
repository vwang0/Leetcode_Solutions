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
        left = '([{'
        right = ')]}'
        stack = []
        for str in s: 
            if s in left:
                stack.append(str)
            else:
                if not stack or left.find(stack.pop())!=right.fin(str):
                    return False
        return not stack

a = Solution()
a.isValid('([)]')



