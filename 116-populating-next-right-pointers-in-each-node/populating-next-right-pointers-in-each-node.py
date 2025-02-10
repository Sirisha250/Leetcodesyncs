# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        # Start with the root node
        queue = [root]
        
        while queue:
            size = len(queue)
            prev = None  # To track previous node in level
            
            for _ in range(size):
                node = queue.pop(0)
                
                # Connect previous node to current node
                if prev:
                    prev.next = node
                prev = node  # Update previous
                
                # Enqueue child nodes
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Mark end of level
            node.next = None
        
        return root
