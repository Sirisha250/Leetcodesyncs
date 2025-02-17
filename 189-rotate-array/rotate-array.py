class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # In case k is larger than the length of nums
        
        # Rotate the array
        nums[:] = nums[-k:] + nums[:-k]

# Example usage:
solution = Solution()

# Test case 1
nums1 = [1, 2, 3, 4, 5, 6, 7]
solution.rotate(nums1, 3)
print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

# Test case 2
nums2 = [-1, -100, 3, 99]
solution.rotate(nums2, 2)
print(nums2)  # Output: [3, 99, -1, -100]
