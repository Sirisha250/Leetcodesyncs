class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32-bit mask to handle negative numbers
        MASK = 0xFFFFFFFF  
        
        while b:
            carry = (a & b) << 1  # Compute carry
            a = (a ^ b) & MASK  # Sum without carry
            b = carry & MASK  # Apply carry
            
        # Handle negative numbers (Python has no fixed int size)
        return a if a <= 0x7FFFFFFF else ~(a ^ MASK)

# Example usage:
obj = Solution()
print(obj.getSum(1, 2))  # Output: 3
print(obj.getSum(2, 3))  # Output: 5
