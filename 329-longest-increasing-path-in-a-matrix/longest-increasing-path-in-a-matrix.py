class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[-1] * cols for _ in range(rows)]  # Memoization table
        directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up

        def dfs(r, c):
            if memo[r][c] != -1:
                return memo[r][c]

            max_len = 1  # The path includes at least this cell
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))

            memo[r][c] = max_len  # Store result in memoization table
            return max_len

        # Compute the longest path for every cell and take the maximum
        return max(dfs(r, c) for r in range(rows) for c in range(cols))

# Test cases
sol = Solution()
print(sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))  # Output: 4
print(sol.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))  # Output: 4
print(sol.longestIncreasingPath([[1]]))                      # Output: 1
