"""
0496. Next Greater Element I
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) :
        n1 = len(nums1)
        n2 = len(nums2)
        nums3 = []
        for i in range(n1):
            a = nums2.index(nums1[i])
            for j in range(a,n2):
                length1 = len(nums3)
                if nums1[i] < nums2[j]:
                    nums3.append(nums2[j])
                    length2 = len(nums3)
                    break
                else:
                    length2 =len(nums3)
            
            if j < n2-1 or (j==n2-1 and length1 < length2):
                continue
            else:
                nums3.append(-1)
        
        return nums3


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) :
        stack, hashmap = list(), dict()
        for i in nums2:
            while len(stack) != 0 and stack[-1] < i:hashmap[stack.pop()] = i
            stack.append(i)
        return [hashmap.get(i,-1) for i in nums1]

