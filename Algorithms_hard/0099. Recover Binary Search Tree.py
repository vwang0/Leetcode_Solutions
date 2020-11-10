"""
0099. Recover Binary Search Tree
Hard

You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

Example 1:

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Stack-based (iterative) inorder traversal solution
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur, prev, drops, stack = root, TreeNode(float('-inf')), [], []      
        while cur or stack:                                                  
            while cur:                                                       
                stack.append(cur)                                            
                cur = cur.left                                               
            node = stack.pop()                                               
            if node.val < prev.val: drops.append((prev, node))               
            prev, cur = node, node.right                                     
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val
    
    def inorder(self, root):
        cur, stack = root, []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            print(node.val)
            cur = node.right

# Morris inorder traversal solution
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur, prev, drops = root, TreeNode(float('-inf')), []                 
        while cur:                                                           
            if cur.left:                                                     
                temp = cur.left                                              
                while temp.right and temp.right != cur: 
                    temp = temp.right    
                if not temp.right:                                           
                    temp.right, cur = cur, cur.left                          
                    continue                                                 
                temp.right = None                                            
            if cur.val < prev.val: drops.append((prev, cur))                 
            prev, cur = cur, cur.right                                       
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val

    def inorderMorris(self, root):
        cur = root
        while cur:
            if cur.left:
                temp = cur.left
                while temp.right and temp.right != cur: 
                    temp = temp.right
                if not temp.right:
                    temp.right, cur = cur, cur.left
                    continue
                temp.right = None
            print(cur.val)
            cur = cur.right


            
