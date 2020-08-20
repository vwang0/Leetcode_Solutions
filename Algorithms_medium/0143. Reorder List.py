"""
0143. Reorder List
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        if fast.next:
            fast = fast.next
        prev = slow
        curr = slow.next
        prev.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        trav = head
        while fast.next:
            tmp1 = trav.next
            tmp2 = fast.next
            trav.next = fast
            fast.next = tmp1
            trav = tmp1
            fast = tmp2
            


        

