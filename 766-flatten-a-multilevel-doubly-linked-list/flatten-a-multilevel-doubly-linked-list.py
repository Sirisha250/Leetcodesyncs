class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        stack = []
        current = head
        
        while current:
            if current.child:
                if current.next:
                    stack.append(current.next)  # Save the next node to revisit later
                
                current.next = current.child  # Connect child to the next pointer
                current.child.prev = current  # Maintain the prev link
                current.child = None  # Remove the child pointer
            
            if not current.next and stack:
                next_node = stack.pop()  # Retrieve the next node
                current.next = next_node
                next_node.prev = current
            
            current = current.next
        
        return head
