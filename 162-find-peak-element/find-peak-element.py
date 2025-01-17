class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                # Peak lies on the left side
                right = mid
            else:
                # Peak lies on the right side
                left = mid + 1
        
        return left

        