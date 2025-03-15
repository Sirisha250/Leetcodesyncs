import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        min_heap = []
        
        # Add all boundary cells to the heap
        for r in range(rows):
            for c in [0, cols - 1]:  # First and last column
                heapq.heappush(min_heap, (heightMap[r][c], r, c))
                visited[r][c] = True
        for c in range(cols):
            for r in [0, rows - 1]:  # First and last row
                if not visited[r][c]:
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        water_trapped = 0

        while min_heap:
            height, r, c = heapq.heappop(min_heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # Water trapped if the neighbor is lower than current height
                    water_trapped += max(0, height - heightMap[nr][nc])
                    # Push updated cell into the heap with new height
                    heapq.heappush(min_heap, (max(height, heightMap[nr][nc]), nr, nc))

        return water_trapped
