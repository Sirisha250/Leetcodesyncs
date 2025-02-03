class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0  # No jumps needed if there's only one element
        
        jumps = 0
        farthest = 0
        current_end = 0

        for i in range(len(nums) - 1):  # Don't need to process the last index
            farthest = max(farthest, i + nums[i])  # Update the farthest we can reach
            
            if i == current_end:  # Time to jump
                jumps += 1
                current_end = farthest  # Update the end of the current jump
                
                if current_end >= len(nums) - 1:  # If we reached or exceeded the last index
                    break
        
        return jumps

# Example usage:
solution = Solution()
print(solution.jump([2,3,1,1,4]))  # Output: 2
print(solution.jump([2,3,0,1,4]))  # Output: 2
""
        