class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:  # If price is increasing, sell
                max_profit += prices[i] - prices[i - 1]

        return max_profit

# Example Usage
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))  # Output: 7
print(sol.maxProfit([1,2,3,4,5]))  # Output: 4
print(sol.maxProfit([7,6,4,3,1]))  # Output: 0

        