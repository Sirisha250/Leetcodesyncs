class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # DP table
        max_side = 0  # Stores max square side length
        
        # Iterate through the matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # First row/column can only have 1x1 squares
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1  # Find min of neighbors
                    
                    max_side = max(max_side, dp[i][j])  # Update max square size
        
        return max_side * max_side  # Return area
