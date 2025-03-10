class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == -1:
                right = mid - 1  # Pick is lower
            else:
                left = mid + 1  # Pick is higher

        