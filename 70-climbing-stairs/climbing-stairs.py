class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        a, b = 1, 2  # Base cases
        for _ in range(3, n + 1):
            a, b = b, a + b  # Fibonacci update
        
        return b

# Example usage:
sol = Solution()
print(sol.climbStairs(2))  # Output: 2
print(sol.climbStairs(3))  # Output: 3
print(sol.climbStairs(4))  # Output: 5
print(sol.climbStairs(5))  # Output: 8
