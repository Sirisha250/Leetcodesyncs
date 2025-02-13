class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head  # Both pointers start at head

        while fast and fast.next:
            slow = slow.next       # Move one step
            fast = fast.next.next  # Move two steps

            if slow == fast:  # Cycle detected
                return True

        return False  # No cycle detected

# Example Usage:
def createLinkedListWithCycle(values, pos):
    if not values:
        return None
    
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]  # Creating the cycle

    return nodes[0]

# Test Cases
solution = Solution()

head1 = createLinkedListWithCycle([3,2,0,-4], 1)
print(solution.hasCycle(head1))  # Output: True

head2 = createLinkedListWithCycle([1,2], 0)
print(solution.hasCycle(head2))  # Output: True

head3 = createLinkedListWithCycle([1], -1)
print(solution.hasCycle(head3))  # Output: False
