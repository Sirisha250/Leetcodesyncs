class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)
        F = sum(i * nums[i] for i in range(n))  # Compute F(0)
        max_value = F

        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            max_value = max(max_value, F)

        return max_value

# Test Cases
solution = Solution()
print(solution.maxRotateFunction([4,3,2,6]))  # Output: 26
print(solution.maxRotateFunction([100]))  # Output: 0
