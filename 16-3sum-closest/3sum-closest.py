class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()  # Sort the array
        closest_sum = float('inf')  # Initialize with infinity
        n = len(nums)

        for i in range(n - 2):  # Iterate, leaving space for two pointers
            left, right = i + 1, n - 1  # Two-pointer setup
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                # Update closest sum if this sum is closer to target
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                if total < target:
                    left += 1  # Increase sum by moving left pointer
                elif total > target:
                    right -= 1  # Decrease sum by moving right pointer
                else:
                    return total  # Exact match found
        
        return closest_sum

# Example usage:
sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1))  # Output: 2
print(sol.threeSumClosest([0,0,0], 1))      # Output: 0
