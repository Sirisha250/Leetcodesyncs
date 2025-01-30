class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0  # Slow pointer

        for j in range(len(nums)):  # Fast pointer
            if nums[j] != val:  # Keep elements that are not equal to val
                nums[i] = nums[j]  
                i += 1  # Move slow pointer
        
        return i  # Length of the modified array
