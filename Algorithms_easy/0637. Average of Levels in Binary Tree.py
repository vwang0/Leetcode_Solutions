"""
0637. Average of Levels in Binary Tree
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode):
        queue = [root]
        res = []
        while queue:
            next_q = []
            cur_sum = 0
            for node in queue:
                cur_sum += node.val
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            res.append(cur_sum/len(queue)*1.0)
            queue = next_q
        return res

