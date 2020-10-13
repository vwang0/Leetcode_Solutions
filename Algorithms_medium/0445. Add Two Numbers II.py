"""
0445. Add Two Numbers II
Medium

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = s2 = 0
        while l1:
            s1 *= 10
            s1 += l1.val
            l1 = l1.next
        while l2:
            s2 *= 10
            s2 += l2.val
            l2 = l2.next
        s3 = s1 + s2
        tail = None
        head = None
        while s3 > 0:
            head = ListNode(s3%10)
            head.next = tail
            tail = head
            s3 //= 10
        return head if head else ListNode(0)


