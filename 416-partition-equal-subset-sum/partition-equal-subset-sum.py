class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False  # If sum is odd, we cannot split evenly
        
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum 0 is always possible
        
        for num in nums:
            for i in range(target, num - 1, -1):  # Traverse backwards
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
