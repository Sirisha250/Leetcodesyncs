class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while True:
            # Check if there are k nodes left to reverse
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # If fewer than k nodes, return result
            
            # Reverse k nodes
            prev, curr = kth.next, prev_group.next
            for _ in range(k):
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            
            # Connect reversed part with previous group
            temp = prev_group.next
            prev_group.next = prev
            prev_group = temp  # Move to next group
            
        return dummy.next

        