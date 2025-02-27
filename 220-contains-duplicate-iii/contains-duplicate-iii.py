from sortedcontainers import SortedList

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        if valueDiff < 0:  # Edge case: absolute difference cannot be negative
            return False

        window = SortedList()  # Maintains a sorted window of at most indexDiff elements

        for i, num in enumerate(nums):
            # Find the smallest number in `window` that is >= nums[i] - valueDiff
            pos = window.bisect_left(num - valueDiff)

            # Check if the found number satisfies |nums[i] - nums[j]| ≤ valueDiff
            if pos < len(window) and abs(window[pos] - num) <= valueDiff:
                return True
            
            # Add current number to window
            window.add(num)

            # Maintain window size ≤ indexDiff
            if i >= indexDiff:
                window.remove(nums[i - indexDiff])

        return False
