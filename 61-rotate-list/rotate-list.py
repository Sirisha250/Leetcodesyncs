class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the linked list
        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1

        # Step 2: Make the list circular by connecting the tail to the head
        last.next = head

        # Step 3: Find the new tail (length - k % length) steps from the head
        k = k % length  # In case k is larger than the length
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # Step 4: Break the circle and return the new head
        new_head = new_tail.next
        new_tail.next = None
        return new_head

        