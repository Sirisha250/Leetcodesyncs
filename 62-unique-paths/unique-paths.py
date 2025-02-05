class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n for _ in range(m)]  # Initialize a grid filled with 1s
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  # Sum of top and left cells
        
        return dp[m-1][n-1]  # Bottom-right cell contains the answer

# Example usage:
sol = Solution()
print(sol.uniquePaths(3, 7))  # Output: 28
print(sol.uniquePaths(3, 2))  # Output: 3

        