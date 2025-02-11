class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')  # Track maximum path sum

        def dfs(node):
            if not node:
                return 0  # Base case: return 0 for null nodes
            
            # Recursively get max path sum from left and right (ignore negatives)
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Path including both left and right (split path)
            current_sum = node.val + left + right

            # Update global max sum
            self.max_sum = max(self.max_sum, current_sum)

            # Return max path sum **without splitting** (must continue upwards)
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum

# Example Usage:
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

sol = Solution()
print(sol.maxPathSum(root1))  # Output: 6
print(sol.maxPathSum(root2))  # Output: 42
