class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        
        # DP table: (m+1) x (n+1), initialized to 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: Any string `s` can match an empty `t` in one way
        for i in range(m + 1):
            dp[i][0] = 1  
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[m][n]  # The answer is in dp[m][n]
