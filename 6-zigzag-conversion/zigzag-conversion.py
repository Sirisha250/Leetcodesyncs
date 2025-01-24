class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge case when numRows is 1 or the string length is less than numRows
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array to hold the strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Traverse the string and place each character in the appropriate row
        for char in s:
            rows[current_row] += char
            
            # Change direction if we hit the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row depending on the direction
            current_row += 1 if going_down else -1
        
        # Join all the rows to get the final result
        return ''.join(rows)

# Test cases
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(solution.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(solution.convert("A", 1))               # Output: "A"
