import math

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets == 1:
            return 0  # No pigs needed if there's only 1 bucket
        
        T = minutesToTest // minutesToDie  # Number of tests each pig can perform
        pigs = 0

        # Find the minimum number of pigs needed
        while (T + 1) ** pigs < buckets:
            pigs += 1
        
        return pigs
