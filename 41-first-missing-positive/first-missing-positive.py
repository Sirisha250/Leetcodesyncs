class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Step 1: Place numbers at their correct indices
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # Swap
        
        # Step 2: Find the first missing positive number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1  # If all are correctly placed, return n + 1

# Example usage:
solution = Solution()
print(solution.firstMissingPositive([1, 2, 0]))        # Output: 3
print(solution.firstMissingPositive([3, 4, -1, 1]))   # Output: 2
print(solution.firstMissingPositive([7, 8, 9, 11, 12])) # Output: 1
