class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        for i in range(n - 1, -1, -1):  # Start from the last digit
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry, return early
            digits[i] = 0  # Set to 0 if it was 9 and carry over
        
        # If we exit the loop, all digits were 9 (e.g., [9,9,9] → [1,0,0,0])
        return [1] + digits

# Example usage:
sol = Solution()
print(sol.plusOne([1,2,3]))  # Output: [1,2,4]
print(sol.plusOne([4,3,2,1]))  # Output: [4,3,2,2]
print(sol.plusOne([9]))  # Output: [1,0]
print(sol.plusOne([9,9,9]))  # Output: [1,0,0,0]
