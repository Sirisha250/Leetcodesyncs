class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]: 
            return
        
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Build the prefix sum matrix
        for i in range(rows):
            for j in range(cols):
                self.prefix_sum[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.prefix_sum[i][j + 1]
                    + self.prefix_sum[i + 1][j]
                    - self.prefix_sum[i][j]
                )

    def sumRegion(self, row1, col1, row2, col2):
        # Using the prefix sum formula to get the sum of a submatrix
        return (
            self.prefix_sum[row2 + 1][col2 + 1]
            - self.prefix_sum[row1][col2 + 1]
            - self.prefix_sum[row2 + 1][col1]
            + self.prefix_sum[row1][col1]
        )

# Example usage
numMatrix = NumMatrix([
    [3, 0, 1, 4, 2], 
    [5, 6, 3, 2, 1], 
    [1, 2, 0, 1, 5], 
    [4, 1, 0, 1, 7], 
    [1, 0, 3, 0, 5]
])

print(numMatrix.sumRegion(2, 1, 4, 3))  # Output: 8
print(numMatrix.sumRegion(1, 1, 2, 2))  # Output: 11
print(numMatrix.sumRegion(1, 2, 2, 4))  # Output: 12
