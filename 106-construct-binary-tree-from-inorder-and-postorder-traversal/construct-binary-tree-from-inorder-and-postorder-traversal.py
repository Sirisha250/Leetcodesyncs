class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        # Last element of postorder is the root
        root_val = postorder.pop()
        root = TreeNode(root_val)  # Use environment's TreeNode

        # Find root index in inorder traversal
        root_index = inorder.index(root_val)

        # Build right subtree first (because we pop from the end of postorder)
        root.right = self.buildTree(inorder[root_index+1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)

        return root  # Return as TreeNode object
