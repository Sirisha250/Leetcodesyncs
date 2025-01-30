class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Two pointers: `i` is the slow pointer, `j` is the fast pointer
        i = 0  
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # When we find a new unique element
                i += 1
                nums[i] = nums[j]  # Move the unique element forward
        
        return i + 1  # The length of unique elements
