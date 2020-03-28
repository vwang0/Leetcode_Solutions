"""
404. Sum of Left Leaves
Find the sum of all left leaves in a given binary tree.
Example:
    3
   / \
  9  20
    /  \
   15   7
There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root: return 0
        stack = [root]
        res = 0
        while stack:
            u = stack.pop()
            if u.left:
                stack.append(u.left)
                if not u.left.left and not u.left.right:
                    res += u.left.val
            if u.right:
                stack.append(u.right)
        return res