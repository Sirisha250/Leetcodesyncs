class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sort the array first
        res = []
        n = len(nums)

        for i in range(n - 2):  # The last two elements are for the two-pointer sum
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            
            left, right = i + 1, n - 1  # Two pointers
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:  # Found a triplet
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate values to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1  # Need a larger sum, move left pointer
                else:
                    right -= 1  # Need a smaller sum, move right pointer
        
        return res

# Example usage:
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))  # Output: [[-1,-1,2],[-1,0,1]]
print(sol.threeSum([0,1,1]))           # Output: []
print(sol.threeSum([0,0,0]))           # Output: [[0,0,0]]
