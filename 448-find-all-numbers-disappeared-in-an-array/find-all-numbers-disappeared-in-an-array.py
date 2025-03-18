class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        # Step 1: Mark visited indices
        for i in range(n):
            index = abs(nums[i]) - 1  # Convert value to index (1-based to 0-based)
            nums[index] = -abs(nums[index])  # Mark as visited (negative)

        # Step 2: Collect indices of positive values
        return [i + 1 for i in range(n) if nums[i] > 0]
