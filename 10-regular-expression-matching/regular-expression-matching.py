class Solution:
    def isMatch(self, s, p):  # Removed type hints for Python 2 compatibility
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):  
                return i == len(s)

            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':  
                memo[(i, j)] = (dp(i, j + 2) or  # Skip "char*"
                                (first_match and dp(i + 1, j)))  
                return memo[(i, j)]

            if first_match:
                memo[(i, j)] = dp(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = False
            return False

        return dp(0, 0)

# Example usage:
sol = Solution()
print(sol.isMatch("aa", "a"))    # Output: False
print(sol.isMatch("aa", "a*"))   # Output: True
print(sol.isMatch("ab", ".*"))   # Output: True

