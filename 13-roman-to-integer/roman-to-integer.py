class Solution:
    def romanToInt(self, s):
        # Roman numeral mappings
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Traverse from right to left
        for char in reversed(s):
            curr_value = roman_map[char]
            
            if curr_value < prev_value:
                total -= curr_value  # Subtract if a smaller numeral precedes a larger one
            else:
                total += curr_value  # Otherwise, add the value
            
            prev_value = curr_value  # Update previous value
        
        return total

# Example usage:
sol = Solution()
print(sol.romanToInt("III"))      # Output: 3
print(sol.romanToInt("LVIII"))    # Output: 58
print(sol.romanToInt("MCMXCIV"))  # Output: 1994
 