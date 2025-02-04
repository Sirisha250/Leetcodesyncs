class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort()  # Sort intervals by start time
        merged = [intervals[0]]  # Initialize with the first interval

        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:  # Overlapping intervals
                merged[-1][1] = max(last_end, end)  # Merge by updating the end time
            else:
                merged.append([start, end])  # Add a new non-overlapping interval

        return merged
