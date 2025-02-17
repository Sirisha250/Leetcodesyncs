class Solution:
    def maxProfit(self, k, prices):
        # If there are no prices or no transactions allowed, return 0 profit
        if not prices or k == 0:
            return 0

        # If k is greater than or equal to half the length of prices,
        # we can complete as many transactions as we want (equivalent to unlimited transactions)
        if k >= len(prices) // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))

        # Create a 2D DP table with (k+1) rows and len(prices) columns
        dp = [[0] * len(prices) for _ in range(k+1)]

        for i in range(1, k+1):
            max_diff = -prices[0]  # This is the max value for (dp[i-1][j] - prices[j])
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i-1][j] - prices[j])

        return dp[k][-1]  # The maximum profit at the last day with at most k transactions

# Example usage:
solution = Solution()
print(solution.maxProfit(2, [2, 4, 1]))  # Output: 2
print(solution.maxProfit(2, [3, 2, 6, 5, 0, 3]))  # Output: 7
