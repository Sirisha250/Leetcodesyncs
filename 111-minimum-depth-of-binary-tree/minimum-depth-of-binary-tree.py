# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0  # Base case: empty tree

        # If one of the subtrees is None, we must take the depth of the non-null subtree
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        # If both subtrees exist, take the minimum of both
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
