"""
347. Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        return [w for w, v in sorted(Counter(nums).items(), key = lambda x: (-x[1], x[0])) [:k]]

from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        items = [ (-value, key) for key, value in c.items() ]
        items.sort()
        return list(map(lambda i: i[1], items[:k]))