class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None (modifies nums in-place)
        """
        # Pointer for the position of the next non-zero element
        non_zero_index = 0  

        # Move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1
