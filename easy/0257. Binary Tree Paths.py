"""
257. Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.
Example:
Input:

   1
 /   \
2     3
 \
  5
Output: ["1->2->5", "1->3"]
Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: 
            return []
        if not root.left or not root.right: 
            return [str(root.val)]
        return [str(root.val) + '->' + i for i in self.rootToLeafPaths(root.left)] +
             [str(root.val) + '->' + i for i in self.rootToLeafPaths(root.right)]
