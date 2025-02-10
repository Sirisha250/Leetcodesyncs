# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(node, path, remainingSum):
            if not node:
                return  # Base case: If node is None, return
            
            # Include current node in the path
            path.append(node.val)
            remainingSum -= node.val  # Subtract the node's value from remaining sum

            # Check if we reached a leaf node and the sum matches
            if not node.left and not node.right and remainingSum == 0:
                result.append(list(path))  # Add a copy of the current path to results

            # Recursively search left and right subtrees
            dfs(node.left, path, remainingSum)
            dfs(node.right, path, remainingSum)

            # Backtrack: Remove the last node before returning
            path.pop()

        dfs(root, [], targetSum)
        return result

        