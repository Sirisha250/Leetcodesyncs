from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_boomerangs = 0

        for i in range(len(points)):
            distance_map = defaultdict(int)

            for j in range(len(points)):
                if i == j:
                    continue
                
                # Compute squared Euclidean distance
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                distance = dx * dx + dy * dy
                
                # Count the occurrences of this distance
                distance_map[distance] += 1

            # Calculate boomerangs using P(k,2) = k * (k-1)
            for count in distance_map.values():
                if count > 1:
                    total_boomerangs += count * (count - 1)

        return total_boomerangs
