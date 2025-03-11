import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = list(nums)  # Store the original array
        self.array = list(nums)  # Copy of the array to modify

    def reset(self):
        """
        :rtype: List[int]
        """
        self.array = list(self.original)  # Restore the original order
        return self.array

    def shuffle(self):
        """
        :rtype: List[int]
        """
        random.shuffle(self.array)  # Shuffle the array randomly
        return self.array
