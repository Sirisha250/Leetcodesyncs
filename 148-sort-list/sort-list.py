class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head  # Base case: Single node or empty list

        # Step 1: Find the middle node
        mid = self.getMiddle(head)
        right_head = mid.next
        mid.next = None  # Break the list into two parts

        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(right_head)

        # Step 3: Merge sorted halves
        return self.merge(left, right)

    def getMiddle(self, head):
        """Find the middle node using slow & fast pointers"""
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow  # Middle node

    def merge(self, left, right):
        """Merge two sorted linked lists"""
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left or right  # Attach remaining nodes
        return dummy.next

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
sorted_head1 = solution.sortList(head1)
print(linkedListToList(sorted_head1))  # Output: [1,2,3,4]

head2 = buildLinkedList([-1,5,3,4,0])
sorted_head2 = solution.sortList(head2)
print(linkedListToList(sorted_head2))  # Output: [-1,0,3,4,5]

head3 = buildLinkedList([])
sorted_head3 = solution.sortList(head3)
print(linkedListToList(sorted_head3))  # Output: []
