class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()  # Sort to handle duplicates
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):  # Base case: found a permutation
                result.append(path[:])  # Store a copy
                return

            for i in range(len(nums)):
                # Skip used elements or duplicate elements in the same depth
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()  # Backtrack
                used[i] = False
        
        backtrack([])
        return result

# Example usage:
solution = Solution()
print(solution.permuteUnique([1,1,2]))  # Output: [[1,1,2], [1,2,1], [2,1,1]]
print(solution.permuteUnique([1,2,3]))  # Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

        