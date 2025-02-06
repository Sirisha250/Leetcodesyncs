class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)  # If <= 2 elements, return as is
        
        slow = 2  # Start from the third position
        
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:  # Allow at most two occurrences
                nums[slow] = nums[fast]
                slow += 1  # Move slow pointer
                
        return slow  # New valid length

# Example test cases
solution = Solution()
nums1 = [1,1,1,2,2,3]
k1 = solution.removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 5, nums = [1,1,2,2,3]

nums2 = [0,0,1,1,1,1,2,3,3]
k2 = solution.removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 7, nums = [0,0,1,1,2,3,3]
