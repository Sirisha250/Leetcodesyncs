# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, next = None, random = None):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        # Dictionary to map old nodes to new nodes
        node_map = {}
        
        # First pass: Create all nodes without links
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        
        # Second pass: Assign next and random pointers
        curr = head
        while curr:
            if curr.next:
                node_map[curr].next = node_map[curr.next]
            if curr.random:
                node_map[curr].random = node_map[curr.random]
            curr = curr.next
        
        return node_map[head]
