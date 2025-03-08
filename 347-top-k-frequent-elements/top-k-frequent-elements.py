from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Count frequency of each element
        freq_map = Counter(nums)

        # Step 2: Use a heap to get the top k elements
        return [num for num, _ in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]
