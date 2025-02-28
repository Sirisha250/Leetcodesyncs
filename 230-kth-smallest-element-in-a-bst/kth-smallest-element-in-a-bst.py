class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        current = root
        count = 0
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left  # Move to leftmost node
            
            current = stack.pop()  # Visit node
            count += 1
            
            if count == k:
                return current.val  # Found the k-th smallest element
            
            current = current.right  # Move to right node

        