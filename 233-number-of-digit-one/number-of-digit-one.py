class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        factor = 1  # Represents 1s, 10s, 100s, etc.
        
        while factor <= n:
            higher = n // (factor * 10)  # Digits to the left
            current = (n // factor) % 10  # Current digit
            lower = n % factor  # Digits to the right
            
            if current == 0:
                count += higher * factor  # Cases where 1 doesn't appear
            elif current == 1:
                count += higher * factor + lower + 1  # Include remainder
            else:
                count += (higher + 1) * factor  # Cases where 1 appears in full set
            
            factor *= 10  # Move to next digit place
        
        return count
