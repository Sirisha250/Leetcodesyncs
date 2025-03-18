class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key):
        """Deletes a node from the BST and returns the new root."""
        if not root:
            return None
        
        # Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  # Node to delete is found
            # Case 1 & 2: Node has one or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Case 3: Node has two children, find inorder successor
            min_larger_node = self.getMin(root.right)
            root.val = min_larger_node.val  # Replace value
            root.right = self.deleteNode(root.right, min_larger_node.val)  # Delete successor
        
        return root
    
    def getMin(self, node):
        """Finds the node with the smallest value in the subtree."""
        while node.left:
            node = node.left
        return node
