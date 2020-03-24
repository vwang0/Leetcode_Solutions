"""
252. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:
Input: [[7,10],[2,4]]
Output: true
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i[0])
        return all([intervals[i][0] >= intervals[i-1][1] for i in range(1, len(intervals))])
