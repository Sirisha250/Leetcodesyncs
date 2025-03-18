from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        
        # dp[i] stores a dictionary with difference as keys and count of sequences ending at i
        dp = [defaultdict(int) for _ in range(n)]
        total_count = 0
        
        # Iterate over each pair (j, i) with j < i
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]  # Common difference
                
                # Count of subsequences ending at j with difference 'diff'
                prev_count = dp[j][diff]
                
                # Update dp[i][diff] by extending sequences from dp[j][diff]
                dp[i][diff] += prev_count + 1
                
                # Only add to total count if it's an arithmetic subsequence (length ≥ 3)
                total_count += prev_count

        return total_count
