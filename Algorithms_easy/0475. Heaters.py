"""
0475. Heaters
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
 

Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
 

Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]):
        houses.sort()
        heaters.sort()
        res, r = 0, 0
        i, j = 0, 0
        m, n = len(houses), len(heaters)
        while i < m and j < n:
            if houses[i] <= heaters[j]:
                r = heaters[j] - houses[i]
                i += 1
            elif j < n-1:
                r = min(heaters[j+1] - houses[i], houses[i] - heaters[j])
                if houses[i] < heaters[j+1]:
                    i += 1
                else:
                    j += 1
            else:
                r = houses[i] - heaters[j]
                i += 1
            res = max(res,r)
        return res
