class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337  # Given modulo
        PHI_MOD = 1140  # Euler's totient function for 1337

        def power_mod(x, y, mod):
            """Computes (x^y) % mod using fast modular exponentiation."""
            result = 1
            x = x % mod  # Reduce x modulo first
            
            while y > 0:
                if y % 2 == 1:
                    result = (result * x) % mod
                x = (x * x) % mod
                y //= 2
            
            return result
        
        # Compute exponent `b` mod 1140
        exponent = 0
        for digit in b:
            exponent = (exponent * 10 + digit) % PHI_MOD  # Reduce modulo 1140

        # Edge case: if exponent becomes 0, use 1140 instead
        if exponent == 0:
            exponent = 1140

        # Compute final result
        return power_mod(a, exponent, MOD)
