class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        
        triangle = [[1]]  # First row is always [1]
        
        for i in range(1, numRows):
            row = [1]  # Start each row with 1
            prev_row = triangle[i - 1]  # Get the previous row
            
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])  # Compute middle values
            
            row.append(1)  # End each row with 1
            triangle.append(row)
        
        return triangle
