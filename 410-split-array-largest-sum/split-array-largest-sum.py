class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canSplit(maxSum):
            subarrays = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > maxSum:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            return True
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid  # Try a smaller max sum
            else:
                left = mid + 1  # Increase the allowed max sum
        
        return left
