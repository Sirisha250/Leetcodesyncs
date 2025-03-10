import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        min_heap = []
        
        # Push first element of each row into the heap
        for i in range(min(n, k)):  # No need to add more than k elements
            heapq.heappush(min_heap, (matrix[i][0], i, 0))
        
        # Extract k smallest elements
        for _ in range(k - 1):
            val, r, c = heapq.heappop(min_heap)
            
            # Push next element in the same row if available
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
        
        return heapq.heappop(min_heap)[0]

        