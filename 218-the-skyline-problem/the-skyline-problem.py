import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # Step 1: Collect all critical events
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))  # Building start
            events.append((right, 0, None))        # Building end
        
        # Step 2: Sort events
        # Sorting rules:
        # 1. Sort by x-coordinate
        # 2. If x is the same, sort by height (negative heights first)
        #    - This ensures taller buildings are processed first
        # 3. If same x and same height, process start before end
        events.sort()

        # Step 3: Process events using a max-heap
        result = []
        heap = [(0, float('inf'))]  # Max-heap (negative height, right boundary)
        prev_height = 0

        for x, neg_h, right in events:
            if neg_h < 0:  # If it's a start event
                heapq.heappush(heap, (neg_h, right))
            else:  # If it's an end event, remove buildings lazily
                while heap and heap[0][1] <= x:
                    heapq.heappop(heap)

            # Get the current max height
            current_height = -heap[0][0]
            if current_height != prev_height:
                result.append([x, current_height])
                prev_height = current_height

        return result

# Example test cases
sol = Solution()

# Test Case 1
buildings1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(sol.getSkyline(buildings1))
# Expected Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

# Test Case 2
buildings2 = [[0,2,3],[2,5,3]]
print(sol.getSkyline(buildings2))
# Expected Output: [[0,3],[5,0]]

# Large Input Test Case
buildings3 = [[i, 20000 - i, i + 1] for i in range(0, 5000, 2)]
print(sol.getSkyline(buildings3))
# This tests performance on a large dataset.
