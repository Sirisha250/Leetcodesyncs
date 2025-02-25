import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # Convert the first k elements into a heap
        
        for num in nums[k:]:
            if num > min_heap[0]:  # Only push if larger than the smallest in heap
                heapq.heappushpop(min_heap, num)
        
        return min_heap[0]  # k-th largest element
