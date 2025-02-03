class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None (modifies matrix in-place)
        """
        n = len(matrix)

        # Step 1: Transpose the matrix (swap rows and columns)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row (flip horizontally)
        for row in matrix:
            row.reverse()
