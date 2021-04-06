"""
1214. Two Sum BSTs
Medium

Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:


Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false
 

Constraints:

The number of nodes in each tree is in the range [1, 5000].
-109 <= Node.val, target <= 109
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def dfs(node):
            return dfs(node.left) | dfs(node.right) | {node.val} if node else set()
        
        q1 = dfs(root1)
        return any(target - a in q1 for a in dfs(root2))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def preorder(root: TreeNode) -> None:
            if not root: return
            seen.add(root.val)
            preorder(root.left)
            preorder(root.right)
            
        def preorder2(root: TreeNode) -> bool:
            if not root: return False
            if target - root.val in seen: return True
            return preorder2(root.left) or preorder2(root.right)    
        
        seen = set()
        preorder(root2)
        return preorder2(root1);

        