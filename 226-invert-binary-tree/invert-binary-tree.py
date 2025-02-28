class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None  # Base case: If the tree is empty, return None
        
        # Swap left and right subtrees
        root.left, root.right = root.right, root.left 
        
        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root  # Return the modified root
