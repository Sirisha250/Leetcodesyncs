import bisect

class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        result = []
        
        for interval in intervals:
            idx = bisect.bisect_left(starts, (interval[1],))
            result.append(starts[idx][1] if idx < len(starts) else -1)
        
        return result
