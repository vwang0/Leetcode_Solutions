"""
0309. Best Time to Buy and Sell Stock with Cooldown
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        pft0, pft1, pft2 = -prices[0], 0, 0
        for i in range(1, n):
            new_pft0 = max(pft0, pft2 - prices[i])
            new_pft1 = pft0 + prices[i]
            new_pft2 = max(pft1, pft2)
            pft0, pft1, pft2 = new_pft0, new_pft1, new_pft2
        return max(pft1, pft2)