class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            elif total < n:
                left = mid + 1
            else:
                right = mid - 1
        return right

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(abs(num))
            else:
                nums[index] = -nums[index]
        return res