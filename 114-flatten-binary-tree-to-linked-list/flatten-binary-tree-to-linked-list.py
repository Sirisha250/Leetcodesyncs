# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None (Modifies tree in-place)
        """
        if not root:
            return
        
        # Keep track of the previous node (starting from None)
        self.prev = None

        def dfs(node):
            if not node:
                return
            
            # Process right subtree first
            dfs(node.right)
            dfs(node.left)

            # Rearrange pointers
            node.right = self.prev
            node.left = None
            self.prev = node  # Move prev pointer to current node
        
        dfs(root)
