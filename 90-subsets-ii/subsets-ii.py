class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()  # Sort to handle duplicates easily

        def backtrack(start, path):
            res.append(list(path))  # Store the current subset
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:  # Skip duplicates
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)  # Recursive call
                path.pop()  # Backtrack

        backtrack(0, [])
        return res
