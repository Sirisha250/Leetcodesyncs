class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, path):
            result.append(path[:])  # Store a copy of the current subset
            
            for i in range(start, len(nums)):
                path.append(nums[i])  # Include current number
                backtrack(i + 1, path)  # Explore further choices
                path.pop()  # Backtrack by removing the last added element

        backtrack(0, [])
        return result

# Example test cases
solution = Solution()
print(solution.subsets([1,2,3]))  # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(solution.subsets([0]))      # Output: [[],[0]]
