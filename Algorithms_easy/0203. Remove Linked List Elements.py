"""
203. Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = ListNode(0)
        prev.next = head
        record = prev
        trav = head
        while trav:
            if trav.val == val:
                prev.next = trav.next
                trav = prev.next
            else:
                prev = trav
                trav = trav.next
        return record.next