class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1  # Base cases
        
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left = dp[root - 1]  # Trees with left subtree
                right = dp[nodes - root]  # Trees with right subtree
                dp[nodes] += left * right
        
        return dp[n]

# Example Usage
sol = Solution()
print(sol.numTrees(3))  # Output: 5
print(sol.numTrees(1))  # Output: 1
