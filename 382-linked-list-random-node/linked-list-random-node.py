import random

class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head  # Store the head reference

    def getRandom(self):
        """
        :rtype: int
        """
        result = None
        node = self.head
        count = 0

        while node:
            count += 1
            # Replace result with probability 1/count
            if random.randint(1, count) == 1:
                result = node.val
            node = node.next
        
        return result
