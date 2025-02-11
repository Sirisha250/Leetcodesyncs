class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy1, profit1 = float('inf'), 0
        buy2, profit2 = float('inf'), 0

        for price in prices:
            buy1 = min(buy1, price)  # First buy
            profit1 = max(profit1, price - buy1)  # First sell
            buy2 = min(buy2, price - profit1)  # Second buy
            profit2 = max(profit2, price - buy2)  # Second sell

        return profit2

# Example Usage
sol = Solution()
print(sol.maxProfit([3,3,5,0,0,3,1,4]))  # Output: 6
print(sol.maxProfit([1,2,3,4,5]))  # Output: 4
print(sol.maxProfit([7,6,4,3,1]))  # Output: 0
