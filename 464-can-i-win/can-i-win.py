class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # If sum of all numbers is less than desiredTotal, player 1 will always lose
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
        
        # Memoization dictionary
        memo = {}

        def dfs(used, current_sum):
            if used in memo:
                return memo[used]

            for i in range(maxChoosableInteger):
                if not (used & (1 << i)):  # If number i+1 is not used
                    if current_sum + (i + 1) >= desiredTotal:  # If picking i+1 wins the game
                        memo[used] = True
                        return True
                    # Recursively check if opponent must lose
                    if not dfs(used | (1 << i), current_sum + (i + 1)):
                        memo[used] = True
                        return True
            
            memo[used] = False
            return False
        
        return dfs(0, 0)  # Start with no numbers picked and sum = 0
