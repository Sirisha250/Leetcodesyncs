class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update min price
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update max profit

        return max_profit

# Example Usage
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))  # Output: 5
print(sol.maxProfit([7,6,4,3,1]))  # Output: 0

        