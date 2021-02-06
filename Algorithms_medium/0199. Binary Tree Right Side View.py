"""
0199. Binary Tree Right Side View
Medium

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
Accepted
332,643
Submissions
607,139
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res, nxtL = [], [root] if root else []
        while nxtL:
            res.append(nxtL[-1].val)
            curL, nxtL = nxtL, []
            for i in curL:
                if i.left:
                    nxtL.append(i.left)
                if i.right:
                    nxtL.append(i.right)
        return res