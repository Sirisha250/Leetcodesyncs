class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        
        # If lengths don't match, return False
        if m + n != len(s3):
            return False
        
        # DP table to store results
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: Empty strings interleave to form empty string
        dp[0][0] = True
        
        # Fill DP table
        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]
        
        return dp[m][n]

# Example Test Cases
sol = Solution()
print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # Output: True
print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # Output: False
print(sol.isInterleave("", "", ""))  # Output: True
