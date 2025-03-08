class Solution:
    def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num  # Smallest element so far
            elif num <= second:
                second = num  # Second smallest element so far
            else:
                return True  # Found a valid triplet

        return False
