class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)  # Choose the minimum coins needed

        return dp[amount] if dp[amount] != float('inf') else -1  # Return answer or -1 if not possible

# Test cases
sol = Solution()
print(sol.coinChange([1,2,5], 11))  # Output: 3 (5 + 5 + 1)
print(sol.coinChange([2], 3))       # Output: -1 (Cannot make amount 3)
print(sol.coinChange([1], 0))       # Output: 0 (Amount is already 0)
