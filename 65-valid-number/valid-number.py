import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Regular expression pattern for a valid number
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        return bool(re.match(pattern, s.strip()))

# Example usage:
sol = Solution()
print(sol.isNumber("0"))       # True
print(sol.isNumber("e"))       # False
print(sol.isNumber("."))       # False
print(sol.isNumber("3.14"))    # True
print(sol.isNumber("-90.5"))   # True
print(sol.isNumber("2e10"))    # True
print(sol.isNumber("1e"))      # False
print(sol.isNumber("e3"))      # False
print(sol.isNumber("99e2.5"))  # False
print(sol.isNumber("--6"))     # False
print(sol.isNumber("-+3"))     # False
print(sol.isNumber("95a54e53"))# False
