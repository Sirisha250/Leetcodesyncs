class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_position(nums, target, find_first):
            left, right = 0, len(nums) - 1
            position = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    position = mid  # Update position
                    if find_first:
                        right = mid - 1  # Keep searching left
                    else:
                        left = mid + 1   # Keep searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return position
        
        return [find_position(nums, target, True), find_position(nums, target, False)]
       