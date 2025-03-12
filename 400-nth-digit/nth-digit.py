class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = 1  # Number of digits in the current range
        count = 9  # Number of integers in the current range
        start = 1  # Starting number of the current range
        
        # Step 1: Find the digit range
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        
        # Step 2: Find the actual number
        num = start + (n - 1) // length  # The number containing the digit
        digit_index = (n - 1) % length  # Index of the digit in the number
        
        # Step 3: Return the specific digit
        return int(str(num)[digit_index])

# Test Cases
solution = Solution()
print(solution.findNthDigit(3))  # Output: 3
print(solution.findNthDigit(11)) # Output: 0
