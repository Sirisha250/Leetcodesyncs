class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start):
            if start == len(nums):  # Base case: found a permutation
                result.append(nums[:])  # Store a copy
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)  # Recurse
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack (undo swap)
        
        backtrack(0)
        return result

# Example usage:
solution = Solution()
print(solution.permute([1,2,3]))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(solution.permute([0,1]))    # Output: [[0,1],[1,0]]
print(solution.permute([1]))      # Output: [[1]]
