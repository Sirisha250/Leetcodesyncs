class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before_head = before = ListNode(0)  # Dummy node for 'before' list
        after_head = after = ListNode(0)    # Dummy node for 'after' list
        
        # Traverse the original list
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        
        after.next = None  # Ensure the 'after' list ends properly
        before.next = after_head.next  # Connect 'before' list to 'after' list
        
        return before_head.next  # Skip the dummy node and return the partitioned list
