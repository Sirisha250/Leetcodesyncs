class Solution:
    def intToRoman(self, num):  # Removed type hints for Python 2 compatibility
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman = ""
        i = 0
        while num > 0:
            while num >= val[i]:
                roman += syb[i]  
                num -= val[i]  
            i += 1  
        
        return roman

# Example usage:
sol = Solution()
print(sol.intToRoman(3749))  # Output: "MMMDCCXLIX"
print(sol.intToRoman(58))    # Output: "LVIII"
print(sol.intToRoman(1994))  # Output: "MCMXCIV"
