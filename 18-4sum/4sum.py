class Solution:
    def fourSum(self, nums, target):
        nums.sort()  # Sort the array
        res = []
        n = len(nums)

        for i in range(n - 3):  # First fixed number
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue

            for j in range(i + 1, n - 2):  # Second fixed number
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates
                    continue
                
                left, right = j + 1, n - 1  # Two-pointer approach
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:  # Found a valid quadruplet
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # Skip duplicate elements
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1  # Need a larger sum, move left pointer
                    else:
                        right -= 1  # Need a smaller sum, move right pointer
        
        return res

# Example usage:
sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2], 0))  # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(sol.fourSum([2,2,2,2,2], 8))      # Output: [[2,2,2,2]]
