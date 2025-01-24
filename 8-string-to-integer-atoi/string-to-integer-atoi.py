class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove leading whitespaces
        s = s.lstrip()
        
        # Check if the string is empty after stripping
        if not s:
            return 0
        
        # Initialize variables
        sign = 1  # Default sign is positive
        result = 0
        i = 0
        
        # Check for optional sign
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            i += 1  # Move to the next character
        
        # Convert characters to integer while ignoring non-digits
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        # Apply sign to the result
        result *= sign
        
        # Return the result within the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result

        