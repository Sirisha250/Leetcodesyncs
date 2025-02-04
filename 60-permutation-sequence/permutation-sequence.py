import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = list(range(1, n + 1))  # List of numbers to use in permutation
        k -= 1  # Convert k to 0-based index
        result = ""

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)  # Factorial of remaining numbers
            index = k // fact  # Find index of the number to place
            result += str(numbers.pop(index))  # Append the number and remove from list
            k %= fact  # Update k for the next iteration

        return result
