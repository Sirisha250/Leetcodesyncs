from collections import defaultdict
from fractions import Fraction

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 2:
            return len(points)

        max_count = 1  # Minimum, at least one point exists
        
        for i in range(len(points)):
            slope_count = defaultdict(int)
            same_point = 0
            local_max = 1  # Count at least the current point itself
            
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if x1 == x2 and y1 == y2:
                    same_point += 1  # Duplicate point
                    continue

                # Compute slope (dy/dx) as a fraction to avoid precision errors
                dx = x2 - x1
                dy = y2 - y1
                slope = Fraction(dy, dx) if dx != 0 else 'inf'  # Vertical line has infinite slope
                
                slope_count[slope] += 1
                local_max = max(local_max, slope_count[slope] + 1)

            max_count = max(max_count, local_max + same_point)  # Include duplicate points

        return max_count

# Test Cases
solution = Solution()

print(solution.maxPoints([[1,1],[2,2],[3,3]]))  # Output: 3
print(solution.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))  # Output: 4

        