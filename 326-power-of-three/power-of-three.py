class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3  # Keep dividing by 3
        return n == 1

# Test cases
sol = Solution()
print(sol.isPowerOfThree(27))  # Output: True (3^3)
print(sol.isPowerOfThree(0))   # Output: False
print(sol.isPowerOfThree(-1))  # Output: False
print(sol.isPowerOfThree(9))   # Output: True (3^2)
print(sol.isPowerOfThree(45))  # Output: False (Not a power of 3)
