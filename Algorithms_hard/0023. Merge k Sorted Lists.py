'''
23. Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Solution 1
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = [(lists[i].val, i) for i in range(len(lists)) if lists[i]]
        heapq.heapify(heap)
        head = None
        while heap:
            nex = heapq.heappop(heap)
            node = ListNode(nex[0])
            index = nex[1]
            if not head:
                head = node
                trav = head
            else:
                trav.next = node
                trav = trav.next
            if lists[index].next:
                lists[index] = lists[index].next
                heapq.heappush(heap, (lists[index].val, index))
        return head 


# Solution 2
class Solution(object):
    def mergeKLists(self, lists):
        head = ListNode(-1)
        cursor = head
        nodes = []
        ListNode.__lt__ = lambda x, y: True if x.val < y.val else False # key statement
        for node in lists:
            if node != None:
                heapq.heappush(nodes, (node.val, node))
        while len(nodes) > 0:
            val, node = heapq.heappop(nodes)
            cursor.next = node
            if node.next:
                heapq.heappush(nodes, (node.next.val, node.next))
            cursor = cursor.next
        return head.next