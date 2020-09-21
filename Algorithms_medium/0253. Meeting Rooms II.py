"""
0253. Meeting Rooms II
similar: 1094, 1109
Medium

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = cur = 0
        for i, v in sorted(x for i, j in intervals for x in [[i, 1], [j, -1]]):
            cur += v
            res = max(res, cur)
        return res



