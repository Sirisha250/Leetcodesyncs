class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._leftmost_inorder(root)
    
    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left
    
    def next(self):
        """
        :rtype: int
        """
        # Pop the top item from the stack
        top_node = self.stack.pop()
        # If the node has a right child, process its leftmost child
        if top_node.right:
            self._leftmost_inorder(top_node.right)
        return top_node.val
    
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
