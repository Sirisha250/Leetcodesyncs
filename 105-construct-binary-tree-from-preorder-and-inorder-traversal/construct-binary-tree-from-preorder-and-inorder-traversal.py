class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        # Root value is the first element in preorder
        root_val = preorder[0]
        root = TreeNode(root_val)  # Use the environment's TreeNode

        # Find root index in inorder
        root_index = inorder.index(root_val)

        # Recursively build left and right subtrees
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])

        return root


