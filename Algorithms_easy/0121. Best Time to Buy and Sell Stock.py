"""
0121. Best Time to Buy and Sell Stock
Array 


Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        low, maxDiff = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                diff = prices[i] - low
                if diff > maxDiff:
                    maxDiff = diff
        return maxDiff


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            cur_profit = price - min_price
            max_profit = max(max_profit, cur_profit)
        return max_profit

# Time: O(N)  Space: O(1)