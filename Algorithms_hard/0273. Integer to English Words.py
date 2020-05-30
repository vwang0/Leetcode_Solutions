"""
0273. Integer to English Words
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""
class Solution:
    def numberToWords(self, num: int):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousand = 'Thousand Million Billion'.split()
        
        def word(num, idx=0):
            if num == 0:
                return []
            if num < 20:
                return [to19[num-1]]
            if num < 100:
                return [tens[num//10-2]] + word(num%10)
            if num < 1000:
                return [to19[num//100-1]] + ['Hundred'] + word(num%100)
            p, r = num//1000, num%1000
            space = [thousand[idx]] if p % 1000 !=0 else []
            return  word(p, idx+1) + space + word(r)
        return ' '.join(word(num)) or 'Zero'      



class Solution:
    def numberToWords(self, num: int) -> str:
        """
        :type num: int
        :rtype: str
        """
        def helper(num):
            if num < 10:
                return dic1[num]
            elif 10 <= num < 20:
                return dic3[num]
            elif num < 100:
                res = []
                q, num = divmod(num, 10)
                res.append(dic2[q*10])
                if num > 0:
                    res.append(" "+dic1[num])
                return "".join(res)
            elif num < 1000:
                q, num = divmod(num, 100)
                if num == 0:
                    return dic1[q]+" "+"Hundred"
                else:
                    return dic1[q]+" "+"Hundred"+" "+helper(num)
            elif num < 1000000:
                q, num = divmod(num, 1000)
                if num == 0:
                    return helper(q)+" "+"Thousand"
                else:
                    return helper(q)+" "+"Thousand"+" "+helper(num)
            elif num < 1000000000:
                q, num = divmod(num, 1000000)
                if num == 0:
                    return helper(q)+" "+"Million"
                else:
                    return helper(q)+" "+"Million"+" "+helper(num)
            else:
                q, num = divmod(num, 1000000000)
                if num == 0:
                    return helper(q)+" "+"Billion"
                else:
                    return helper(q)+" "+"Billion"+" "+helper(num)  
                
        if num == 0:
            return "Zero"
        
        dic1 = {9:"Nine", 8:"Eight", 7:"Seven", 6:"Six", 
                5:"Five", 4:"Four", 3:"Three", 2:"Two", 1:"One"}
        dic2 = {90:"Ninety", 80:"Eighty", 70:"Seventy", 60:"Sixty", 
                50:"Fifty", 40:"Forty", 30:"Thirty", 20:"Twenty"} 
        dic3 = {19:"Nineteen", 18:"Eighteen", 17:"Seventeen", 
                16:"Sixteen", 15:"Fifteen", 14:"Fourteen", 13:"Thirteen", 
                12:"Twelve", 11:"Eleven", 10:"Ten"}
        
        return helper(num)