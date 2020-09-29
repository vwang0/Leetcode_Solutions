"""
1213. Intersection of Three Sorted Arrays
Easy

Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(set(arr1) & set(arr2) & set(arr3))


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        combined = arr1 + arr2 + arr3
        get_dict = {}
        
        for x in combined:
            if x in get_dict:
                get_dict[x] += 1
            else:
                get_dict[x] = 1
                
        return sorted([key for key, val in get_dict.items() if val == 3])



        