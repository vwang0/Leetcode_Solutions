"""
0105. Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        def helper(pre_left: int, pre_right: int, in_left: int, in_right: int):
            if pre_left > pre_right: return None
            pre_root = pre_left
            in_root = idx_map[preorder[pre_root]]
            root = TreeNode(preorder[pre_root])
            size_left = in_root - in_left
            root.left = helper(pre_left + 1, pre_left + size_left, in_left,
                               in_root - 1)
            root.right = helper(pre_left + size_left + 1, pre_right,
                                in_root + 1, in_right)
            return root

        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(preorder) - 1, 0, len(preorder) - 1)
