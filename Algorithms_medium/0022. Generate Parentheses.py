"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate 
all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution:
    def generateParenthesis(self, n):
        def gen(L, R, s):
            if R >= L >= 0:
                if R == 0: self.result.append(s)
                gen(L - 1, R, s + '(')
                gen(L, R - 1, s + ')')
        self.result = []
        gen(n, n, '')
        return self.result

