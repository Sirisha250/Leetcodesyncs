class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                right = mid - 1  # Move left to find a higher H-Index
            else:
                left = mid + 1  # Move right to find more valid papers
        
        return n - left  # Final H-Index
