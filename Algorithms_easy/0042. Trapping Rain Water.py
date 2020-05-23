'''
0042. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
class Solution:
    def trap(self, height):
        if height == []: return 0
        max_num = max(height)
        max_point, res, start = height.index(max_num), 0, 0
        for i in range(1, max_point):
            if height[start] > height[i]:
                res += height[start] - height[i]
            else:
                start = i
        end = len(height) - 1
        j = end - 1
        while j > max_point:
            if height[end] > height[j]:
                res += height[end] - height[j]
            else:
                end = j
            j -= 1
        return res


