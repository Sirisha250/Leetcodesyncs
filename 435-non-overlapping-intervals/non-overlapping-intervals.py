class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])  # Sort by end time
        non_overlapping = 0
        end = float('-inf')
        
        for interval in intervals:
            if interval[0] >= end:
                non_overlapping += 1
                end = interval[1]
        
        return len(intervals) - non_overlapping
