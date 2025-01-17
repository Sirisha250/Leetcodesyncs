class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x  # The square root of 0 or 1 is itself.

        left, right = 0, x
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                result = mid  # Update the result since mid is a valid candidate.
                left = mid + 1
            else:
                right = mid - 1

        return result

        