"""
256. Paint House
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
Note:
All costs are positive integers.
Example:
Input: [[17,2,17],[16,16,5],[14,3,19]]
[17,2,17] represents cost of painting in red, blue and green for house 0
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.
"""
  
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        eachCost = [0] * 3
        for cost in costs:
            eachCost = [min(eachCost[:j] + eachCost[j+1:]) + cost[j] for j in range(3)]
        return min(eachCost)

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        lastMinCost = [0,0,0]
        for cost in costs:
            newMinCost = [0,0,0]
            newMinCost[0] = cost[0] + min(lastMinCost[1], lastMinCost[2])
            newMinCost[1] = cost[1] + min(lastMinCost[2], lastMinCost[0])
            newMinCost[2] = cost[2] + min(lastMinCost[0], lastMinCost[1])
            lastMinCost = newMinCost
        return min(lastMinCost)