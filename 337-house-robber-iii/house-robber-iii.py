class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        memo = {}

        def dfs(node):
            if not node:
                return 0

            if node in memo:
                return memo[node]

            # Option 1: Rob this node, skip its direct children
            rob_current = node.val
            if node.left:
                rob_current += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                rob_current += dfs(node.right.left) + dfs(node.right.right)

            # Option 2: Skip this node, take the best from children
            skip_current = dfs(node.left) + dfs(node.right)

            # Store the maximum value obtained at this node
            memo[node] = max(rob_current, skip_current)
            return memo[node]

        return dfs(root)
