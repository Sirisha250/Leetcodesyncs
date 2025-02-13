class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head  # Base case: Single node or empty list

        dummy = ListNode(0)  # Dummy head to simplify insertions
        current = head  # Pointer to traverse the unsorted list

        while current:
            prev = dummy  # Start from the dummy node
            next_node = current.next  # Store next node before modifying links
            
            # Find the correct position in sorted list
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            # Insert current node in the correct place
            current.next = prev.next
            prev.next = current
            
            # Move to the next node
            current = next_node

        return dummy.next  # Return the sorted list (ignoring dummy node)

# Helper function to convert list to linked list
def buildLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list
def linkedListToList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Cases
solution = Solution()

head1 = buildLinkedList([4,2,1,3])
sorted_head1 = solution.insertionSortList(head1)
print(linkedListToList(sorted_head1))  # Output: [1,2,3,4]

head2 = buildLinkedList([-1,5,3,4,0])
sorted_head2 = solution.insertionSortList(head2)
print(linkedListToList(sorted_head2))  # Output: [-1,0,3,4,5]
