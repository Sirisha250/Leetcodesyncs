class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = min(nums)  # Find the minimum element
        return sum(num - min_val for num in nums)  # Sum of differences
