class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Initialize a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # Previous pointer starts at dummy
        current = head  # Current pointer starts at head
        
        while current:
            # Skip all duplicates
            if current.next and current.val == current.next.val:
                # Move current forward until we reach the last duplicate
                while current.next and current.val == current.next.val:
                    current = current.next
                # Skip the last duplicate node
                prev.next = current.next
            else:
                prev = prev.next  # Move prev pointer when current node is unique
            current = current.next  # Always move current forward
        
        return dummy.next  # Return the modified list starting from the head

# Helper function to convert a list to a linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print linked list
def print_linkedlist(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# Example test cases
solution = Solution()

# Test case 1
head1 = list_to_linkedlist([1,2,3,3,4,4,5])
result1 = solution.deleteDuplicates(head1)
print(print_linkedlist(result1))  # Output: [1, 2, 5]

# Test case 2
head2 = list_to_linkedlist([1,1,1,2,3])
result2 = solution.deleteDuplicates(head2)
print(print_linkedlist(result2))  # Output: [2, 3]

        