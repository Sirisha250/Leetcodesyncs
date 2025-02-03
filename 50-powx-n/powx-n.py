class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Handle the case when n is negative
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:  # If n is odd
                result *= x
            x *= x  # Square the base
            n //= 2  # Integer division by 2 (reduce exponent)
        
        return result

# Example usage:
solution = Solution()
print(solution.myPow(2.00000, 10))  # Output: 1024.00000
print(solution.myPow(2.10000, 3))  # Output: 9.26100
print(solution.myPow(2.00000, -2))  # Output: 0.25000

        