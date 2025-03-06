class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head  # Connect odd and even lists
        return head

# Helper function to convert list to LinkedList
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print LinkedList
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Test cases
sol = Solution()
head1 = create_linked_list([1,2,3,4,5])
head2 = create_linked_list([2,1,3,5,6,4,7])

print_linked_list(sol.oddEvenList(head1))  # Output: [1,3,5,2,4]
print_linked_list(sol.oddEvenList(head2))  # Output: [2,3,6,7,1,5,4]
