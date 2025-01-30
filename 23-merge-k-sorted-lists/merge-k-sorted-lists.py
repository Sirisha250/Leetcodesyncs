from heapq import heappush, heappop

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []
        
        # Push initial nodes of all lists into the heap
        for i, l in enumerate(lists):
            if l:
                heappush(min_heap, (l.val, i, l))  # Store (value, index, node)
        
        dummy = ListNode(0)
        curr = dummy
        
        while min_heap:
            val, i, node = heappop(min_heap)  # Get the smallest node
            curr.next = node
            curr = curr.next
            
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next

        