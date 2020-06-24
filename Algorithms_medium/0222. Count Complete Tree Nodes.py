"""
0222. Count Complete Tree Nodes
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""
class Solution:
    def countNodes(self, root: TreeNode):
        if not root:
            return 0

        # Find tree final level (Tree Height)
        self.root = root
        node = root
        self.level = -1
        while node:
            node = node.left
            self.level += 1

        # Start Binary Search
        left = 0
        right = 2 ** self.level - 1

        # If it's full binary tree then directly return # nodes
        if self.check_node(right):
            return 2 ** self.level + right

        while left < right - 1:
            mid = (left + right) // 2
            if self.check_node(mid):
                left = mid
            else:
                right = mid

        return 2 ** self.level + left

    def check_node(self, idx):
        node = self.root
        # The order if search path could be regarded as binary value converted from index
        # Make sure the len(order) = self.level
        order = format(idx, '0{}b'.format(self.level))
        for num in order:
            if num == '0':
                node = node.left
            else:
                node = node.right
        return True if node else False