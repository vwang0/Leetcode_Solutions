"""
0938. Range Sum of BST
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int):
        def dfs(root):
            if not root:
                return
            if L <= root.val <= R:
                self.res += root.val
            if L <= root.val:
                dfs(root.left)
            if R >= root.val:
                dfs(root.right)
        self.res = 0
        dfs(root)
        return self.res        


class Solution:
    def rangeSumBST(self, root, L, R):
        return root and self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R) + (L <= root.val <= R) * root.val or 0