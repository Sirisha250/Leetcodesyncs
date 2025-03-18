from collections import Counter

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # Step 1: Store all sums of nums1 and nums2 in a hash map
        sum_count = Counter(a + b for a in nums1 for b in nums2)
        
        # Step 2: Find complements from nums3 and nums4
        count = sum(sum_count[-(c + d)] for c in nums3 for d in nums4)
        
        return count
