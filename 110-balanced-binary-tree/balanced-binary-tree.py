# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def checkHeight(node):
            if not node:
                return 0  # Height of an empty tree is 0
            
            left_height = checkHeight(node.left)
            right_height = checkHeight(node.right)

            # If any subtree is unbalanced, propagate -1 up
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1

        return checkHeight(root) != -1  # If -1 is returned, it's unbalanced

        