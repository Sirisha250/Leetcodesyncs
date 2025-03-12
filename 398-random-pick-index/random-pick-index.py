import random

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.index_map = {}  # Store indices of each number
        
        for i, num in enumerate(nums):
            if num not in self.index_map:
                self.index_map[num] = []
            self.index_map[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.index_map[target])  # Pick random index

# Test Cases
solution = Solution([1, 2, 3, 3, 3])
print(solution.pick(3))  # Should return 2, 3, or 4 randomly
print(solution.pick(1))  # Should return 0
print(solution.pick(3))  # Should return 2, 3, or 4 randomly
