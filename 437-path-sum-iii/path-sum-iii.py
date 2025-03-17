from collections import defaultdict

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            count = prefix_sums[curr_sum - targetSum]
            
            prefix_sums[curr_sum] += 1
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            prefix_sums[curr_sum] -= 1  # Backtrack
            
            return count
        
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case to handle sum from root
        return dfs(root, 0)
