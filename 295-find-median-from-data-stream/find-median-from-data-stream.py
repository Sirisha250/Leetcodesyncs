import heapq

class MedianFinder(object):

    def __init__(self):
        # Max heap (invert values to simulate max heap using min heap)
        self.low = []  
        # Min heap (stores the larger half of numbers)
        self.high = []  

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Step 1: Push to max heap first (invert sign to simulate max heap)
        heapq.heappush(self.low, -num)

        # Step 2: Ensure max heap root is <= min heap root
        if self.low and self.high and (-self.low[0] > self.high[0]):
            heapq.heappush(self.high, -heapq.heappop(self.low))

        # Step 3: Balance the heaps if needed
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self):
        """
        :rtype: float
        """
        # If even count, return average of middle two
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) / 2.0
        # If odd count, return middle element
        return -self.low[0]
