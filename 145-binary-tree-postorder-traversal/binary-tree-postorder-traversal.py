class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, node, result):
        if not node:
            return
        self.dfs(node.left, result)   # Traverse left subtree
        self.dfs(node.right, result)  # Traverse right subtree
        result.append(node.val)       # Visit root node

# Helper function to build a binary tree from a list (level order)
def buildTree(values):
    if not values:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in values]
    queue = [nodes[0]]
    front = 0

    for i in range(1, len(nodes), 2):
        parent = queue[front]
        front += 1

        if nodes[i] is not None:
            parent.left = nodes[i]
            queue.append(nodes[i])

        if i + 1 < len(nodes) and nodes[i + 1] is not None:
            parent.right = nodes[i + 1]
            queue.append(nodes[i + 1])

    return nodes[0]

# Test Cases
solution = Solution()

root1 = buildTree([1, None, 2, 3])
print(solution.postorderTraversal(root1))  # Output: [3, 2, 1]

root2 = buildTree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
print(solution.postorderTraversal(root2))  # Output: [4, 6, 7, 5, 2, 9, 8, 3, 1]

root3 = buildTree([])
print(solution.postorderTraversal(root3))  # Output: []

root4 = buildTree([1])
print(solution.postorderTraversal(root4))  # Output: [1]
