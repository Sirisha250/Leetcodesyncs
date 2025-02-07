class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0  # Invalid case

        n = len(s)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1  # Base cases

        for i in range(2, n + 1):
            one_digit = int(s[i-1:i])   # Last 1 digit
            two_digits = int(s[i-2:i])  # Last 2 digits

            if 1 <= one_digit <= 9:
                dp[i] += dp[i-1]  # Single digit valid
            
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]  # Two-digit valid

        return dp[n]
