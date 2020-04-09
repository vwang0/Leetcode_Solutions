"""
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path 
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        if not root: 
            return 0
        elif not root.left and not root.right: 
            return 1
        else:
            q = [(root, 1)]
            while q: 
                node, depth = q.pop(0)
                if node and not node.left and not node.right: 
                    return depth
                if node and node.left: 
                    q.append([node.left, depth+1])
                if node and node.right:
                    q.append([node.right, depth+1])


class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
