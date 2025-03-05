class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        hold = -prices[0]  # Max profit when holding a stock
        sold = 0  # Max profit when we just sold
        cooldown = 0  # Max profit when in cooldown

        for i in range(1, n):
            prev_hold, prev_sold, prev_cooldown = hold, sold, cooldown

            hold = max(prev_hold, prev_cooldown - prices[i])  # Buy or keep holding
            sold = prev_hold + prices[i]  # Sell stock
            cooldown = max(prev_cooldown, prev_sold)  # Cooldown or stay in cooldown

        return max(sold, cooldown)  # Max profit can't be from "hold" state

# Example test cases
sol = Solution()
print(sol.maxProfit([1,2,3,0,2]))  # Output: 3
print(sol.maxProfit([1]))          # Output: 0
