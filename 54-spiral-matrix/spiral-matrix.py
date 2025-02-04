class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        while matrix:
            result += matrix.pop(0)  # Take the first row
            if matrix and matrix[0]:  
                for row in matrix:
                    result.append(row.pop())  # Take the last element of each row
            if matrix:
                result += matrix.pop()[::-1]  # Take the last row in reverse order
            if matrix and matrix[0]:  
                for row in matrix[::-1]:
                    result.append(row.pop(0))  # Take the first element of each row in reverse order
        return result
