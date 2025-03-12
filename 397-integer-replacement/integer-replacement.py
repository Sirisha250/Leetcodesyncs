class Solution(object):
    def __init__(self):
        self.memo = {}  # Store results for faster lookup

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n in self.memo:
            return self.memo[n]

        if n % 2 == 0:
            self.memo[n] = 1 + self.integerReplacement(n // 2)
        else:
            self.memo[n] = 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

        return self.memo[n]

# Test Cases
solution = Solution()
print(solution.integerReplacement(8))  # Output: 3
print(solution.integerReplacement(7))  # Output: 4
print(solution.integerReplacement(4))  # Output: 2
