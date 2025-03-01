class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:  # Keep summing digits until num is a single digit
            num = sum(int(digit) for digit in str(num))
        return num
