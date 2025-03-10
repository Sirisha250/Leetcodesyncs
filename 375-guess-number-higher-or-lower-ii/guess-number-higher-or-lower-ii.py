class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def dp(l, r):
            if l >= r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            
            min_cost = float('inf')
            for x in range(l, r + 1):
                cost = x + max(dp(l, x - 1), dp(x + 1, r))
                min_cost = min(min_cost, cost)
            
            memo[(l, r)] = min_cost
            return min_cost
        
        return dp(1, n)

        