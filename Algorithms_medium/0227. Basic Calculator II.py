"""
0227. Basic Calculator II
Medium

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""
class Solution:
    def calculate(self, s: str) -> int:
        
        num = 0
        pre_op = '+'
        s += '+'
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == ' ':
                pass
            else:
                if pre_op == '+':
                    stack.append(num)
                if pre_op == '-':
                    stack.append(-num) 
                if pre_op == '*':
                    op = stack.pop()
                    stack.append(op*num)                    
                if pre_op == '/':
                    op = stack.pop()
                    stack.append(op//num)      
            num = 0
            pre_op = c
        return sum(stack)
            
        num = 0
        pre_op = '+'
        s += '+'
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == ' ':
                    pass
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    operant = stack.pop()
                    stack.append(operant*num)
                elif pre_op == '/':
                    operant = stack.pop()
                    stack.append(math.trunc(operant/num))
                num = 0
                pre_op = c
        return sum(stack)