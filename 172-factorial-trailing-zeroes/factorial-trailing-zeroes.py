class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n >= 5:
            n //= 5  # Count the number of multiples of 5
            count += n  # Add the number of multiples of 5
        return count
