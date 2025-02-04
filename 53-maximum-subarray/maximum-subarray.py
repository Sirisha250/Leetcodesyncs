class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]  # Initialize max_sum with the first element
        current_sum = nums[0]  # Initialize current sum with the first element

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])  # Either start new subarray or extend current one
            max_sum = max(max_sum, current_sum)  # Update max_sum if we find a larger sum

        return max_sum
