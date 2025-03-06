class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None (modify nums in-place)
        """
        nums.sort()
        mid = (len(nums) - 1) // 2  # Middle index of the smaller half
        small_half = nums[:mid + 1]  # Left half (smaller numbers)
        large_half = nums[mid + 1:]  # Right half (larger numbers)
        
        # Fill odd indices with larger values, even indices with smaller values
        nums[::2] = small_half[::-1]  # Reverse to get correct order
        nums[1::2] = large_half[::-1]  # Reverse to get correct order

# Test cases
sol = Solution()
nums1 = [1,5,1,1,6,4]
sol.wiggleSort(nums1)
print(nums1)  # Output: [1,6,1,5,1,4] or similar valid result

nums2 = [1,3,2,2,3,1]
sol.wiggleSort(nums2)
print(nums2)  # Output: [2,3,1,3,1,2] or similar valid result
 