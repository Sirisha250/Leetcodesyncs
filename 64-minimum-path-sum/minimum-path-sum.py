class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        # Initialize the first row and column
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]  # Fill first column (only downward moves)
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]  # Fill first row (only rightward moves)

        # Compute the minimum path sum for the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[m-1][n-1]  # Bottom-right corner holds the result

# Example usage:
sol = Solution()
print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Output: 7
print(sol.minPathSum([[1,2,3],[4,5,6]]))  # Output: 12

        