class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:  
                left = mid + 1  # Minimum is on the right side
            elif nums[mid] < nums[right]:  
                right = mid  # Minimum could be mid itself
            else:  
                right -= 1  # Remove duplicate uncertainty
        
        return nums[left]
