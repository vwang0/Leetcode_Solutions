"""
0314. Binary Tree Vertical Order Traversal
Medium

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
Example 4:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        data = defaultdict(list)
        def dfs(node, x, y):
            if not node:
                return
            data[x].append((y, node.val))
            dfs(node.left, x - 1, y + 1)
            dfs(node.right, x + 1, y + 1)            
        dfs(root, 0, 0)        
        result = []
        for x in sorted(data.keys()):
            result.append([v for y, v in sorted(data[x])])
        
        return result

