class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sum = [0] * (len(nums) + 1)
        
        # Build prefix sum array
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

# Example Usage:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))  # Output: 1
print(numArray.sumRange(2, 5))  # Output: -1
print(numArray.sumRange(0, 5))  # Output: -3
