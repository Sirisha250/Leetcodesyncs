from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        result = []
        dq = deque()  # Stores indices of elements in the current window

        for i in range(len(nums)):
            # Remove elements not within the sliding window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove elements from the back that are smaller than the current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index to deque
            dq.append(i)

            # Append max of the current window (the front of deque) to result
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
