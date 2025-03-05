class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]  # Add virtual boundaries
        n = len(nums)
        memo = {}  # Dictionary for memoization
        
        def dp(left, right):
            if left + 1 == right:  # No balloon left in this range
                return 0
            if (left, right) in memo:  # Return memoized result
                return memo[(left, right)]
            
            max_coins = 0
            for i in range(left + 1, right):  # Try bursting balloon i last
                coins = nums[left] * nums[i] * nums[right]
                coins += dp(left, i) + dp(i, right)  # Solve left and right subproblems
                max_coins = max(max_coins, coins)
            
            memo[(left, right)] = max_coins  # Store result in memo
            return max_coins

        return dp(0, n - 1)

# Example test cases
sol = Solution()
print(sol.maxCoins([3,1,5,8]))  # Output: 167
print(sol.maxCoins([1,5]))      # Output: 10
