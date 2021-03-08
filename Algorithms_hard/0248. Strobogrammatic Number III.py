"""
0248. Strobogrammatic Number III
Hard


Given two strings low and high that represent two integers low and high where low <= high, return the number of strobogrammatic numbers in the range [low, high].

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: low = "50", high = "100"
Output: 3
Example 2:

Input: low = "0", high = "0"
Output: 1
 

Constraints:

1 <= low.length, high.length <= 15
low and high consist of only digits.
low <= high
low and high do not contain any leading zeros except for zero itself.
"""
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        maps={"0":"0","1":"1","6":"9","8":"8","9":"6"}
        cl,ch=len(low), len(high)
        if cl>ch or (cl==ch and low>high): return 0
        
        ans=["","0","1","8"]
        count=0
        while ans:
            tmp=[]
            for w in ans:
                if len(w)<ch or (len(w)==ch and w<=high):
                    if len(w)>cl or (len(w)==cl and w>=low):  
                        if len(w)>1 and w[0]=="0":##leading zeros
                            pass
                        else:
                            count+=1
                    
                    if ch-len(w)>=2:                
                        for key in maps:
                            res=key+w+maps[key]
                            tmp.append(res)
            ans=tmp
        return count




class Solution:
    res = 0
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        for length in range(len(low),len(high)+1):
            self.dfsHelper(low,high, length, "")
            self.dfsHelper(low,high, length, "1")
            self.dfsHelper(low,high, length, "8")
            self.dfsHelper(low,high, length, "0")
        return self.res
            
        
        
    def dfsHelper(self,low,high,length,path):
        if len(path) > length:
            return
        if len(path) == length:
            if len(path) != 1 and path[0] == '0':
                return
            else:
                if int(path) >= int(low) and int(path) <= int(high):
                    self.res +=1
                return
        self.dfsHelper(low,high, length, '0'+path+'0')
        self.dfsHelper(low,high, length, '6'+path+'9')
        self.dfsHelper(low,high, length, '9'+path+'6')
        self.dfsHelper(low,high, length, '8'+path+'8')
        self.dfsHelper(low,high, length, '1'+path+'1')