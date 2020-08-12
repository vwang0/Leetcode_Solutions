"""
0501. Find Mode in Binary Search Tree
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode):
        dict_t = {}
        res = []
        self.dfs(root, dict_t)
        if len(dict_t.values()) == 0:
            return res
        max_t = max(dict_t.values())
        for key in dict_t:
            if dict_t[key] == max_t:
                res.append(key)
        return res

    def dfs(self, root, dict_t):
        if root is None:
            return
        if not root.val in dict_t:
            dict_t[root.val] = 1
        else:
            dict_t[root.val] += 1
        self.dfs(root.left, dict_t)
        self.dfs(root.right, dict_t)