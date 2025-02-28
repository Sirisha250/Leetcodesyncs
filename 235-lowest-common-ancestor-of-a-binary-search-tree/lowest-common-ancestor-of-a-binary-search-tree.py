class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left  # Move to the left subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right  # Move to the right subtree
            else:
                return root  # Found the LCA
        return None  # Should never reach here if p and q are in the tree
