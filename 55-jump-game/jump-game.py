class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0  # Farthest index we can reach
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False  # If we reach an index beyond max_reach, we fail
            max_reach = max(max_reach, i + jump)  # Update max reach
            if max_reach >= len(nums) - 1:
                return True  # If we can reach or surpass the last index, return True
        return False
