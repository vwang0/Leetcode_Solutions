"""
0092. Reverse Linked List II
Medium

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # if not head: return None
        left, right = head, head
        stop = False
        
        def recurseReveres(right, m, n):
            nonlocal left, stop
            if n == 1: return 0
            right = right.next
            if m > 1:
                left = left.next

            recurseReveres(right, m - 1, n - 1)

            if left == right or right.next == left:
                stop = True
            if not stop:
                left.val, right.val = right.val, left.val
                left = left.next
        
        recurseReveres(right, m, n)
        return head# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # if not head: return None
        left, right = head, head
        stop = False
        
        def recurseReveres(right, m, n):
            nonlocal left, stop
            if n == 1: return 0
            right = right.next
            if m > 1:
                left = left.next

            recurseReveres(right, m - 1, n - 1)

            if left == right or right.next == left:
                stop = True
            if not stop:
                left.val, right.val = right.val, left.val
                left = left.next
        
        recurseReveres(right, m, n)
        return head
    