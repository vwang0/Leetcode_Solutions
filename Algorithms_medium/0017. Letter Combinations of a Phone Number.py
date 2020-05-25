"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number 
could represent.

A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, 
your answer could be in any order you want.

"""
class Solution(object):
    def letterCombinations(self, digits):                
        mapping = {
                    '2':'abc', 
                    '3':'def', 
                    '4':'ghi', 
                    '5':'jkl',                   
                    '6':'mno', 
                    '7':'pqrs', 
                    '8':'tuv', 
                    '9':'wxyz'
                    }
        if not digits: return []
        return reduce(lambda resultList, digit: [x + y for x in resultList for y in mapping[digit]], digits, [''])


class Solution:
    def letterCombinations(self, digits: str):
        num2char = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if len(digits) == 0 or '1' in digits: 
            return []
        res = ['']
        for i in digits:
            res = [k+j for k in res for j in num2char[i]]
        return res
