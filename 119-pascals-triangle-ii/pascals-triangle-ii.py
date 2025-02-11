class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]  # Initialize the first element as 1
        for k in range(1, rowIndex + 1):
            row.append(row[-1] * (rowIndex - k + 1) // k)
        return row

# Example Usage
sol = Solution()
print(sol.getRow(3))  # Output: [1, 3, 3, 1]
print(sol.getRow(0))  # Output: [1]
print(sol.getRow(1))  # Output: [1, 1]

        