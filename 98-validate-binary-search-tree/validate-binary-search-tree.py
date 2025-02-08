# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, min_val, max_val):
            if not node:
                return True  # Empty tree is valid

            if not (min_val < node.val < max_val):
                return False  # Violates BST property
            
            # Check left and right subtrees with updated constraints
            return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)

        return helper(root, float('-inf'), float('inf'))
