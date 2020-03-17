"""
538. Convert BST to Greater Tree
Given a Binary Search Tree (BST), convert it to a Greater Tree 
such that every key of the original BST is changed to 
the original key plus sum of all keys greater than the original key 
in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
Note: This question is the same as 1038: 
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        self.sum = 0

        def dfs(root):
            if not root:
                return

            dfs(root.right)
            root.val += self.sum
            self.sum = root.val
            dfs(root.left)

        dfs(root)         
        return root    
            

