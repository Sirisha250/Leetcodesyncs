import math

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))  # Count of perfect squares ≤ n

# Test cases
sol = Solution()
print(sol.bulbSwitch(3))  # Output: 1
print(sol.bulbSwitch(0))  # Output: 0
print(sol.bulbSwitch(1))  # Output: 1
print(sol.bulbSwitch(10)) # Output: 3 (Bulbs at positions 1, 4, and 9 remain on)

        