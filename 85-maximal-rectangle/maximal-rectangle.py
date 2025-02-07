class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        # Number of rows and columns
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols  # Histogram heights
        max_area = 0  # Store max area
        
        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)  # Append 0 to ensure processing of all heights
            
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
            heights.pop()  # Restore original heights
            return max_area
        
        # Iterate through rows
        for row in matrix:
            for j in range(cols):
                # Update histogram
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            
            # Find max rectangle area in the updated histogram
            max_area = max(max_area, largestRectangleArea(heights))
        
        return max_area

        