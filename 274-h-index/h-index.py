class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)  # Sort in descending order
        h = 0
        
        for i, c in enumerate(citations):
            if c >= i + 1:  # At least (i+1) papers have >= (i+1) citations
                h = i + 1
            else:
                break  # If condition breaks, we have found our H-Index
        
        return h
