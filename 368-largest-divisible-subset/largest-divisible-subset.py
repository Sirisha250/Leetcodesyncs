class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        nums.sort()  # Sort the numbers
        n = len(nums)
        dp = [1] * n  # dp[i] stores the size of the largest subset ending at index i
        parent = [-1] * n  # To reconstruct the subset
        
        max_size, max_index = 1, 0
        
        # Fill DP table
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > max_size:
                max_size, max_index = dp[i], i
        
        # Reconstruct the subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = parent[max_index]
        
        return result[::-1]  # Reverse to get the correct order

# Example usage:
obj = Solution()
print(obj.largestDivisibleSubset([1,2,3]))     # Output: [1,2] or [1,3]
print(obj.largestDivisibleSubset([1,2,4,8]))  # Output: [1,2,4,8]
