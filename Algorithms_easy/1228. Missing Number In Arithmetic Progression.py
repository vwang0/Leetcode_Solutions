"""
1228. Missing Number In Arithmetic Progression
Easy

In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

Then, a value from arr was removed that was not the first or last value in the array.

Return the removed value.

Example 1:

Input: arr = [5,7,11,13]
Output: 9
Explanation: The previous array was [5,7,9,11,13].
Example 2:

Input: arr = [15,13,12]
Output: 14
Explanation: The previous array was [15,14,13,12].

Constraints:

3 <= arr.length <= 1000
0 <= arr[i] <= 10^5
"""
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return (min(arr) + max(arr)) * (len(arr) + 1) // 2 - sum(arr)

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        diff = (arr[-1] - arr[0]) // n
        lo, hi = 0, n
        while lo < hi:
            mi = (lo + hi) >> 1
            if arr[mi] == arr[0] + mi * diff:
                lo = mi + 1
            else:
                hi = mi
        return arr[0] + lo * diff        


