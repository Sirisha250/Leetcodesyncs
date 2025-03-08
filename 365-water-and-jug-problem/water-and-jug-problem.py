from fractions import gcd  # Use fractions.gcd instead of math.gcd

class Solution(object):
    def canMeasureWater(self, x, y, target):
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """
        if target > x + y:
            return False
        return target % gcd(x, y) == 0  # Use gcd from fractions module

# Example usage:
obj = Solution()
print(obj.canMeasureWater(3, 5, 4))  # Output: True
print(obj.canMeasureWater(2, 6, 5))  # Output: False
print(obj.canMeasureWater(1, 2, 3))  # Output: True
