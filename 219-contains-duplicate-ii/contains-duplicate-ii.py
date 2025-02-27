class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set()  # HashSet to store elements in the current window
        
        for i in range(len(nums)):
            if nums[i] in seen:
                return True  # Found a duplicate within the window
            
            seen.add(nums[i])  # Add current element to the set
            
            if len(seen) > k:  # Keep window size at most k
                seen.remove(nums[i - k])  # Remove the leftmost element
        
        return False
