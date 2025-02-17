class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator // denominator)  # Exact division, return as string
        
        result = []
        if (numerator < 0) ^ (denominator < 0):  # Handle negative signs
            result.append('-')
        
        numerator, denominator = abs(numerator), abs(denominator)
        result.append(str(numerator // denominator))  # Integer part
        result.append('.')  # Decimal point

        remainder_map = {}
        remainder = numerator % denominator

        while remainder and remainder not in remainder_map:
            remainder_map[remainder] = len(result)  # Store the index of remainder
            remainder *= 10
            result.append(str(remainder // denominator))  # Append next digit
            remainder %= denominator  # Update remainder
        
        if remainder in remainder_map:  # If remainder repeats, insert parentheses
            index = remainder_map[remainder]
            result.insert(index, '(')
            result.append(')')

        return ''.join(result)
