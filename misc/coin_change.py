"""
Coin change
given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.
Input: amount = 25, coins = [1, 2, 5]
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dic = {0:1}
        for coin in coins:
            for i in range(amount+1):
                dic[i] =dic.get(i,0) + dic.get(i-coin,0)
        return dic.get(amount,0)


amount = 25
coins = [1, 2, 5]
a = Solution()
a.change(amount, coins)
# 42