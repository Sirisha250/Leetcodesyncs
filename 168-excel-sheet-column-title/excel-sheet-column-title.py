class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []
        
        while columnNumber > 0:
            columnNumber -= 1  # Adjust the number to fit in 0-25 range (A=0, B=1, ...)
            result.append(chr(columnNumber % 26 + ord('A')))  # Convert to character
            columnNumber //= 26  # Move to the next "digit"
        
        return ''.join(result[::-1])  # Reverse the result for correct order
