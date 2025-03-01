class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(node, path, result):
            if not node:
                return
            
            path += str(node.val)  # Append current node value
            
            if not node.left and not node.right:  # Leaf node
                result.append(path)  # Add the path to the result list
            else:
                path += "->"  # Add arrow for non-leaf nodes
                dfs(node.left, path, result)
                dfs(node.right, path, result)
        
        result = []
        dfs(root, "", result)
        return result
