class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Example usage:
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))  # True
print(sol.containsDuplicate([1,2,3,4]))  # False
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # True
