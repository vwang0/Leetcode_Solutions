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
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths(kid)] or [str(root.val)]


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        stack = [(root,str(root.val))]
        res = []
        while stack:
            node, path = stack.pop()
            if node.left:
                stack.append((node.left, path+"->"+str(node.left.val)))
            if node.right:
                stack.append((node.right, path+"->"+str(node.right.val)))
            if not node.left and not node.right:
                res.append(path)
        return res