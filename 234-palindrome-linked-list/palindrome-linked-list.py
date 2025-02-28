class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True  # A single-node or empty list is always a palindrome
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # Step 3: Compare the first and second half
        left, right = head, prev  # prev now points to the head of reversed second half
        while right:  # Only need to compare the second half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
