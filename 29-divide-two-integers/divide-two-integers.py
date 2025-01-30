class Solution:
    def divide(self, dividend, divisor):
        # Handle edge case of overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Handle overflow case
        
        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        
        result = 0
        # Keep doubling the divisor and subtracting it from dividend
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):  # Shift left to double the divisor
                temp <<= 1  # Double the divisor
                multiple <<= 1  # Double the multiplier
                
            # Subtract the large divisor multiple and update result
            dividend -= temp
            result += multiple
        
        # Apply the sign to the result
        return sign * result
